# backend/app.py
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()

def create_app(testing=False, mongo_uri=None):
    app = Flask(__name__)
    CORS(app)

    if testing:
        client = MongoClient(mongo_uri)
        db = client["test-db"]
    else:
        MONGO_USER = os.getenv('MONGO_USER')
        MONGO_PASS = os.getenv('MONGO_PASS')
        MONGO_HOST = os.getenv('MONGO_HOST')
        MONGO_DB = os.getenv('MONGO_DB')
        MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:27017/{MONGO_DB}"
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB]

    users_collection = db['users']

    @app.route('/api/employees', methods=['GET'])
    def get_employees():
        employees = []
        for emp in users_collection.find():
            emp['_id'] = str(emp['_id'])
            employees.append(emp)
        return jsonify(employees)

    @app.route('/api/employees', methods=['POST'])
    def add_employee():
        data = request.json
        try:
            data['salary'] = float(data.get('salary', 0))
        except (ValueError, TypeError):
            return jsonify({'error': 'Salary must be a valid number'}), 400

        result = users_collection.insert_one(data)
        new_employee = users_collection.find_one({'_id': result.inserted_id})
        new_employee['_id'] = str(new_employee['_id'])
        return jsonify(new_employee), 201

    @app.route('/api/employees/<id>', methods=['PUT'])
    def update_employee(id):
        data = request.json
        data.pop('_id', None)
        try:
            data['salary'] = float(data.get('salary', 0))
        except (ValueError, TypeError):
            return jsonify({'error': 'Salary must be a valid number'}), 400

        result = users_collection.update_one({'_id': ObjectId(id)}, {'$set': data})
        if result.matched_count == 0:
            return jsonify({'error': 'Employee not found'}), 404
        return jsonify({'message': 'Employee updated successfully'})

    @app.route('/api/employees/<id>', methods=['DELETE'])
    def delete_employee(id):
        result = users_collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({'error': 'Employee not found'}), 404
        return jsonify({'message': 'Employee deleted successfully'})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
