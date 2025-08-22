## Launch EC2 "t2.micro" Instance and In Sg, Open port "5000" for Python Application 
# Backend-Python Application server

## Install python
```
sudo yum update -y
sudo yum install git -y
sudo yum install python3 -y
sudo yum install python3-pip -y
```

## Get the Code

```
git clone https://github.com/digistackops-python-org/Python-3-tier-UMS-Local.git
sudo chown -R ec2-user:ec2-user /home/ec2-user/Python-3-tier-UMS-Local
cd Python-3-tier-UMS-Local
```
Switch branch

```
git checkout 02-Local-setup-Prod
```
# Backend Setup
```
cd backend
```
## Setup your Application Database by executing "initdb.js" script from Application-server

Step:1 ==> install "mongo-Client" for communicate with Mongo Database

```
sudo vim /etc/yum.repos.d/mongodb-org-8.0.repo
```
```
[mongodb-org-8.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/8.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-8.0.asc
```
To install "Mongo-Shell" to communicate with Mongo database
```
sudo yum update -y
sudo yum install -y mongodb-mongosh
```
Step:2 ==> Execute your "init.sql" script for your Application DB setup

```
mongosh "mongodb://<DB-Private-IP>:27017/admin" < initdb.js
```
Create connection file ".env" for DB connection
Dont push ".env" to your SCM for security 
```
sudo vim .env
```
```
MONGO_USER=appuser
MONGO_PASS=Pa55Word
MONGO_HOST=your_db_private_ip
MONGO_DB=user-account
```
Install Dependencies
```
pip install -r requirements.txt
```
Start Backend Application
```
pip install gunicorn
```
To run these Backend Application up and Running we use Linux service
```
which gunicorn
sudo cp -r  ~/.local/bin/gunicorn /usr/local/bin/
```

```
sudo vim /etc/systemd/system/backend.service
```
```
[Unit]
Description=Gunicorn Flask App
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/home/ec2-user/Python-3-tier-UMS-Local/backend
ExecStart=/usr/local/bin/gunicorn --bind 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```
Enable backend service
```
sudo systemctl daemon-reload
sudo systemctl enable backend
sudo systemctl start backend
sudo systemctl status backend
```
