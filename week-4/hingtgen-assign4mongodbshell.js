/**
	Title: hingtgen-assign4mongodbshell.js
    Author: Shane Hingtgen
    Date: 4/12/23
    Description: MongoDB Shell Scripts for the users collection.
    Work Cited:
    Web 335 Assign_4
    Web 335 mongosh guide
    MongoDB https://www.mongodb.com/docs/manual/core/index-single/
    MongoDB https://www.mongodb.com/docs/mongodb-shell/write-scripts/
 */

// find specific user documents
db.users.find(); //finds all in the document
db.users.find({ email: "jbach@me.com" }); //finds that specific email
db.users.find({ lastName: "Mozart" }); //finds that specific last name
db.users.find({ firstName: "Richard" }); //finds that specific first name
db.users.find({ employeeId: "1010" }); //finds that specific employee id
