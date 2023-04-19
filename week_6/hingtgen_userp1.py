# =================================================================================================================
# ; Title: Exercise 6.3 - Python with MongoDB, Part 1
# ; Author: Shane Hingtgen
# ; Bellevue University
# ; Date: 04/17/2023
# ; Description: In this exercise learn to use Python to connect to MongoDB
# ; Work Cited:
#   Python for Beginners https://www.youtube.com/watch?v=kqtD5dpn9C8&t=3594s
#   Web 335 Exercise 6
#   Web 335 Python Guide
# =================================================================================================================

# import mongoclient
from pymongo import MongoClient

# build connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.ut5xprd.mongodb.net/?retryWrites=true&w=majority")

# configure a variable to access the web335DB
db = client["web335DB"]

print(client)

print("List of all documents in the users collection")
# this will display a list of all documents in the users collection
for user in db.users.find():
    print(user)

# added print to easier see in terminal
print("Printing employeeId 1011")
# Displays a document where the employeeId is 1011
print(db.users.find_one({"employeeId": "1011"}))

# added print to easier see in terminal
print("Printing lastName Mozart")
# Displays a document with the lastName Mozart
print(db.users.find_one({"lastName": "Mozart"}))