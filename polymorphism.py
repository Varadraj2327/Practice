#polymorphism = Greek word that means to have many forms or faces
#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance = An object could be treated of the same types as a parent class
#               2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
        

class Square(Shape):
    def __init__(self, side):
        self.side =side
    
    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height                                              

shapes = [Circle(5), Square(3), Triangle(6, 7)]

for shape in shapes:
    print(f"{shape.area()}cm²")