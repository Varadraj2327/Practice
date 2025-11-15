# object = A "bundle" of related attributes (variables) and methods (functions)
#          ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("BMW", "M5", 2025, "Yellow", False)
car2 = Car("Toyota", "M4", 1990, "Black", True)

car1.drive()
