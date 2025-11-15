#class variable = Shared among all instancees of a class
#                 Defined outside the constructor
#                 Allow you to share data among all object created from the class

class Student:

    class_year = 2327
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Joe", 30)
student2 = Student("Dex", 32)
student3 = Student("Varadraj", 19)

print(f"My class of {Student.class_year} has {Student.num_students} student")
