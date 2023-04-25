# =================================================================================================================
# ; Title: Exercise 6.3 - Python with MongoDB, Part 2
# ; Author: Shane Hingtgen
# ; Bellevue University
# ; Date: 04/17/2023
# ; Description: In this exercise learn to use Python to connect to MongoDB
# ; Work Cited:
#   Web 335 Exercise 7
#   Web 335 Python Guide
# =================================================================================================================
# import mongoclient
from pymongo import MongoClient
import datetime

# build connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.ut5xprd.mongodb.net/?retryWrites=true&w=majority")

# configure a variable to access the web335DB
db = client["web335DB"]

print(client)

# creating a new user document
shane = {
    "firstName": "Shane",
    "lastName": "Hingtgen",
    "employeeId": "999",
    "email": "shane@email.com",
    "datecreated": datetime.datetime.utcnow()
}

# adding the new user document to the users collection
shane_user_id = db.users.insert_one(shane).inserted_id
print(shane_user_id)

# verifying new user document was added to the users collection
print(db.users.find_one({"employeeId": "999"}))

# update the email address of the user document we just created
db.users.update_one(
    {"employeeId": "999"},
    {
    "$set": {
        "email": "sah@email.com"
    }
    }
)

# prove the that email address has been updated
print(db.users.find_one({"employeeId": "999"}))

# delete the new users document we just added
result = db.users.delete_one({
    "employeeId": "999"
})
# print the results of the query
print(result)

# prove that it was delete
print(db.users.find_one({"employeeId": "999"}))