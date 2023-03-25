# =================================================================================================================
# ; Title: Exercise 3.3 - Python Variables and Functions
# ; Author: Shane Hingtgen
# ; Bellevue University
# ; Date: 03/25/2023
# ; Description: In this exercise we create functions that add, subtract, divide and multiply
# ; Work Cited:
#   Web 335 Python Guide
#   Python for Beginners https://www.youtube.com/watch?v=kqtD5dpn9C8&t=3594s
#   Bellevue University https://bellevue.mediaspace.kaltura.com/media/Function+Returns/1_3w0ut032
#   Web 335 Exercise 3
#   If Else https://www.programiz.com/python-programming/if-elif-else
# =================================================================================================================
# add function with two parameters
def add(x, y):
    return x + y

# subtract function with two parameters
def subtract(x, y):
    return x - y

# divide function with two parameters
def divide(x, y):
    return x / y

# multiply function with two parameters
def multiply(x, y):
    return x * y

# values and choices for calculator
val1 = int(input("First Value: "))
choice = input(
"""
Select Function: 
a. Add
b. Subtract
c. Multiply
d. Divide                
""")
val2 = int(input("Second Value: "))

# if else statement that will call the functions based on choice
if choice == "a":
    total = add(val1, val2)
    print(val1, "+", val2, "is", total)
elif choice == "b":
    total = subtract(val1, val2)
    print(val1, "-", val2, "is", total)
elif choice == "c":
    total = multiply(val1, val2)
    print(val1, "*", val2, "is", total)
elif choice == "d" and val1 == 0 or val2 == 0:
    print("Undefined") #prints undefined if val1 or val2 is = 0, cannot divide by 0
elif choice == "d":
    total = divide(val1, val2)
    print(val1, "/", val2, "is", total)
else:
    print("Please enter choice of a, b, c or d") #if choice doesn't match criteria it prints message