use admin;

db.createUser({
  user: "appuser",
  pwd: "Pa55Word",
  roles: [
    { role: "readWrite", db: "user-account" }
  ]
});

use user-account;
db.createCollection("users")
