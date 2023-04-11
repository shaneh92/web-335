/**
	Title: projections.js
    Author: Shane Hingtgen
    Date: 4/11/23
    Description: MongoDB Shell Scripts for the users collection.
    Work Cited:
    Web 335 Assign_5
    Web 335 GitHub Examples
 */

// a query to add a new user
db.users.insert({
  firstName: "Max",
  lastName: "Richter",
  employeeId: "1227",
  email: "maxrich@email.com",
  dateCreated: new Date(),
});

// a query to update Mozarts email
db.users.update({ employeeId: "1009" }, { $set: { email: "mozart@me.com" } });

//prove it worked
db.users.find({ lastName: "Mozart" });

// a query that lists all the documents within the collection with projections
db.users.find({}, { firstName: 1, lastName: 1, email: 1 });
