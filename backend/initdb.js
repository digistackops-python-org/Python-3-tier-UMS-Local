// Switch DB properly (hyphenated DB name)
var db = db.getSiblingDB("user-account");

// Create application user
db.createUser({
  user: "appuser",
  pwd: "Pa55Word",
  roles: [
    { role: "readWrite", db: "user-account" }
  ]
});

// Create collection
db.createCollection("users");

// Insert seed data
db.users.insertMany([
  {
    name: "venkatesh",
    email: "venkatesh@sapsecops.com",
    designation: "DevSecOps Engineer",
    salary: 1500000
  },
  {
    name: "chaitanya",
    email: "chaitanya@sapsecops.com",
    designation: "QA Engineer",
    salary: 1200000
  },
  {
    name: "padol",
    email: "padol@sapsecops.com",
    designation: "SAP Developer",
    salary: 1100000
  },
  {
    name: "pandu",
    email: "pandu@sapsecops.com",
    designation: "Database Admin",
    salary: 1000000
  },
  {
    name: "Ganesh",
    email: "ganesh@sapsecops.com",
    designation: "Manager",
    salary: 1300000
  }
]);

print("✅ Database user-account initialized successfully");
