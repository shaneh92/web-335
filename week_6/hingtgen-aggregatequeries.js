/**
	Title: Assignment 6.2 Aggregate Queries
    Author: Shane Hingtgen
    Date: 4/17/23
    Description: This week we learn about Aggregate Queries
    Work Cited:
    Web 335 Assign_6
    Web 335 mongosh guide
 */

// A query to show a list of documents in houses
db.houses.find();

// A query to show a list of documents in students
db.students.find();

//A query to add a document to students collection
db.students.insert({
  firstName: "Shane",
  lastName: "Hingtgen",
  studentId: "s1019",
  houseId: "h1009",
});

// A query to prove it was added
db.students.find({ lastName: "Hingtgen" });

// Delete the query we just made
db.students.deleteOne({ lastName: "Hingtgen" });

// Proof it was deleted
db.students.find({ lastName: "Hingtgen" });

// Query to show list of students by house
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "studentsHousing",
    },
  },
]);

// query to show list of students in house Gryffindor
db.houses.aggregate([
  {
    $match: {
      mascot: "Lion",
    },
  },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "studentsHousing",
    },
  },
]);

// A query to show a list of students for Eagle mascot
db.houses.aggregate([
  {
    $match: {
      mascot: "Eagle",
    },
  },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "studentsHousing",
    },
  },
]);
