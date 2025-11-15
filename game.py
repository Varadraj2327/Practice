# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

students = {"Joe", "Johan", "Varadraj", "Yuuchi"}

student = input("Enter the name as the student: ")

if  student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not persent")