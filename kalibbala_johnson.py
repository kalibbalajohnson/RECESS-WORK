# Object Oriented Programming
# classes
# objects
# en
# in
# pol
# abstraction

# classes are blueprints for creating new types of data structures.
# class car
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Balance: {self.balance}")

# Example usage:
account = BankAccount("123456789", "John Doe", 1000)
account.display_balance()  # Output: Account Balance: 1000

account.deposit(500)  # Output: Deposited 500. New balance: 1500
account.withdraw(200)  # Output: Withdrew 200. New balance: 1300
account.display_balance()  # Output: Account Balance: 1300

# class rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Example usage:
rectangle = Rectangle(5, 3)
print(rectangle.height)
print(rectangle.width)

print(rectangle.area())  # Output: 15
print(rectangle.perimeter())  # Output: 16

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

# Example usage:
student = Student("John", 16, "10th Grade")
student.print_info()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f" My Name: {self.name}")
        print(f"My Age: {self.age}")

# Example usage:
person1 = Person("John Doe", 25)
person2 = Person("John Doe", 25)
print(person1.name)
print(person1.age)

person1.print_details()
person1.print_details()

# Exercise
# calculate the are and circumference of a circle 
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def circumference(self):
        return 2 * 3.14 * self.radius
circle = Circle(7)
print(circle.radius)
print(circle.circumference())
print(circle.area())

# Exercise
# calculate and display the employee bonus(0.5) of salary (employee: 150000, employee: 230000)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_details(self):
        print(f"My Name: {self.name}")
        print(f"My Salary: {self.salary}")
        print(f"My Bonus: {self.salary * 0.15}")
emp1 = Employee("Johnson", 150000)
emp2 = Employee("Kalibbala", 230000)
emp1.print_details()
emp2.print_details()

# Ecapsulation
# example with bank account

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

# Create a bank account with an initial balance of $1000
account = BankAccount("123456789", 1000)

# Deposit $500 into the account
account.deposit(500)

# Withdraw $200 from the account
account.withdraw(200)

# Get the account balance and account number
balance = account.get_balance()
account_number = account.get_account_number()

print(f"Account Number: {account_number}")
print(f"Current Balance: ${balance}")

# Exercise2: convert temperature(37 celcius) celsius to Fahreinheit
class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    def to_fahrenheit(self):
        return (self._celsius * 9/5) + 32

    def get_celsius(self):
        return self._celsius
# Create a temperature converter with Celsius temperature of 37
converter = TemperatureConverter(37)

# Convert Celsius to Fahrenheit
fahrenheit = converter.to_fahrenheit()

# Get the Celsius temperature
celsius = converter.get_celsius()

print(f"Celsius: {celsius}°C")
print(f"Fahrenheit: {fahrenheit}°F")

print("")

print("----------------Assignment--------------")

# Assignment1: show encapsulation with employee information to give a pay
#  incrementation (salary with employee information to new_salary)eg from 850000 to 1000000
class Employee:
    def __init__(self, name, salary, role):
        self._name = name
        self._salary = salary
        self._role = role

    @property
    def salary(self):
        return self._salary

    def increment_salary(self, percentage):
        increment_amount = (percentage / 100) * self._salary
        self._salary += increment_amount

# Example usage
employee = Employee("John Doe", 850000, "Software Engineer") 
print(f"old salary: UGX {employee.salary}")

employee.increment_salary(20)

print(f"new salary: UGX {employee.salary}")
