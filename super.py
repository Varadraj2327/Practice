# super() = Function used in a child to call methods from a parent calss (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, colour, is_filled):
         self.colour = colour
         self.is_filled = is_filled

    def describe(self):
         print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self):
         print(f"The area of circle is {3.14 * self.radius * self.radius} cm^2")
         super().describe()
    
    

class Square(Shape):
        def __init__(self, colour, is_filled, width):
            super().__init__(colour, is_filled)
            self.width = width

class Triangle(Shape):
        def __init__(self, colour, is_filled, width, height):
            super().__init__(colour, is_filled)
            self.width = width
            self.height = height

circle = Circle("yellow", True, 5)
square = Square("Blue", False, 10)



circle.describe()