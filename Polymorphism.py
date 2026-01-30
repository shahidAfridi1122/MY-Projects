class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()



class Car:
    def move(self):
        print("Car is moving")

class Bike:
    def move(self):
        print("Bike is moving")

class Truck:
    def move(self):
        print("Truck is moving")

vehicles = [Car(), Bike(), Truck()]

for vehicle in vehicles:
    vehicle.move()


import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def print_area(shape):
    print("Area:", shape.area())

rect = Rectangle(5, 4)
circle = Circle(3)

print_area(rect)
print_area(circle)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)

result = v1 + v2
print(result)



from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, hours_worked, rate_per_hour):
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour

employees = [
    FullTimeEmployee(50000),
    PartTimeEmployee(120, 300)
]

for emp in employees:
    print("Salary:", emp.calculate_salary())
