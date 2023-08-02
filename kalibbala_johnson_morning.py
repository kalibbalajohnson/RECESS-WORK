# INHERITENCE

# Example 1
class Animal:
    def eat(self):
        print("The animal is eating.")

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("Meow!")

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

# Creating instances of the subclasses
animal = Animal()
cat = Cat("Whiskers")
dog = Dog("Buddy")

# Using the eat method from the Animal class
cat.eat()
dog.eat()
animal.eat()
# Using the subclass-specific methods
cat.meow()
dog.bark()


# Example 2
class Vehicle:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def display_info(self):
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")

    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def __init__(self, color, model):
        super().__init__(color, model)

    def display_info(self):
        print("Car Information:")
        super().display_info()

    def honk(self):
        print("Beep beep!")

# Creating an instance of the Car class
car = Car("Red", "Toyota")

# Using the display_info method from the Car class
car.display_info()

# Using the move method from the Vehicle class
car.move()

# Using the honk method from the Car class
car.honk()

# Exercise 3
# demostrate using inheritance to calculate area and perimeter of circle and rectangle with  shape super class 

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculating area and perimeter for Circle
circle_area = circle.area()
circle_perimeter = circle.perimeter()

print("Circle:")
print("Area:", circle_area)
print("Perimeter:", circle_perimeter)

# Calculating area and perimeter for Rectangle
rectangle_area = rectangle.area()
rectangle_perimeter = rectangle.perimeter()

print("Rectangle:")
print("Area:", rectangle_area)
print("Perimeter:", rectangle_perimeter)

# Multiple inheritence

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

class Flyable:
    def fly(self):
        print("Flying...")

class Bird(Animal, Flyable):
    def __init__(self, name):
        super().__init__(name)

    def chirp(self):
        print("Chirp chirp!")

# Creating an instance of Bird
bird = Bird("Sparrow")

# Accessing methods from Animal class
bird.eat()  # Output: Sparrow is eating...

# Accessing methods from Flyable class
bird.fly()  # Output: Flying...

# Accessing methods from Bird class
bird.chirp()  # Output: Chirp chirp!


# Method Overriding ?
class Animal:
    def eat(self):
        print("Animal eating")

class Dog(Animal):
    def eat(self):
        print("Dog eating")

class Cat(Animal):
    def eat(self):
        print("Dog eating")

def eat_animal(animal):
       animal.eat()       

animal= Animal()
dog = Dog()
cat = Cat()

eat_animal(dog)
eat_animal(cat)
eat_animal(animal)


# POLYMORPHISM

# method Overriding 

class Shape:
    def area(self):
     pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculating area and perimeter for Circle
circle_area = circle.area()
circle_perimeter = circle.perimeter()

print("Circle:")
print("Area:", circle_area)
print("Perimeter:", circle_perimeter)

# Calculating area and perimeter for Rectangle
rectangle_area = rectangle.area()

print("Rectangle:")
print("Area:", rectangle_area)
print("Perimeter:", rectangle_perimeter)




# method Overloading
class Adder:
    def add_two_numbers(self, num1, num2):
        return num1 + num2

    def add_three_numbers(self, num1, num2, num3):
        return num1 + num2 + num3

# Create an instance of Adder
adder = Adder()

# Adding two numbers
result1 = adder.add_two_numbers(2, 3)
print(result1)  

# Adding three numbers
result2 = adder.add_three_numbers(2, 3, 4)
print(result2) 


# ABSTRACTION

class Vehicle:
    def start(self):
        pass

    def stop(self):
        pass

class Truck(Vehicle):
    def start(self):
        print("Truck is starting...")

    def stop(self):
        print("Truck is stopping...")

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

# Creating instances of Truck and Car
truck = Truck()
car = Car()

# Starting and stopping the truck
truck.start()  # Output: Truck is starting...
truck.stop()   # Output: Truck is stopping...

# Starting and stopping the car
car.start()    # Output: Car is starting...
car.stop()     # Output: Car is stopping...

# Exercise Demonstrate  abstraction in calculating area and 
# perimeter of a circle and rectangle as subclasses of shape

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculating area and perimeter of the circle
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()
print("Circle Area:", circle_area)             # Output: Circle Area: 78.53981633974483
print("Circle Perimeter:", circle_perimeter)   # Output: Circle Perimeter: 31.41592653589793

# Calculating area and perimeter of the rectangle
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()
print("Rectangle Area:", rectangle_area)             # Output: Rectangle Area: 24
print("Rectangle Perimeter:", rectangle_perimeter)   # Output: Rectangle Perimeter: 20







