#Inheritance = Allow a class to inherit attributes and method from another class
#              Helps with code reuseability and extensibility
#              class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Bhau!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    pass

dog = Dog("Frank")
cat = Cat("Mr. Wiskerson")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

dog.speak()

