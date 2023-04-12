# =================================================================================================================
# ; Title: Exercise 5.3 - Python
# ; Author: Shane Hingtgen
# ; Bellevue University
# ; Date: 04/11/2023
# ; Description: In this exercise we create two lists, one to iterate over the list and print it, the other to iterate over the list and print based on what day it is
# ; Work Cited:
#   Python for Beginners https://www.youtube.com/watch?v=kqtD5dpn9C8&t=3594s
#   Web 335 Exercise 5
#   W3 Schools https://www.w3schools.com/python/python_lists_loop.asp
#   W3 Schools https://www.w3schools.com/python/python_conditions.asp
# =================================================================================================================

# a list of 5 hobbies
hobbies = ["Hunting", "Fishing", "Gaming", "Kayaking", "Movie Night with my Family"]

# iterating over list of hobbies to print to console
for i in hobbies:
    print(i)

# a list of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# for loop iterating over list of days
# for i in days:
#     if i == "Sunday" :
#         print("Day off, enjoy your hobbies!")
#     elif i == "Saturday":
#         print("Day off, enjoy your hobbies!")
#     else : 
#         print("It's a workday")

# for loop iterating over list of days based off instructions
for i in days:
    if i == "Sunday":
        print("It's Sunday and no work, enjoy your hobbies!")
    elif i == "Monday":
        print("It's Monday and we have to work.")
    elif i == "Tuesday":
        print("It's Tuesday and we have to work.")
    elif i == "Wednesday":
        print("It's Wednesday and we have to work.")
    elif i == "Thursday":
        print("It's Thursday and we have to work.")
    elif i == "Friday":
        print("It's Friday and we have to work.")
    elif i == "Saturday":
        print("It's Saturday and no work, enjoy your hobbies!")