# class BankAccount:
#     def __init__(self):
#         self.__balance = 1000

#     def deposit(self, amount):
#         self.ammount= int(input("Enter ammount to deposit: "))
#         self.__balance += amount
#         print("Total balance after Deposit: ",self.__balance)

#     def withdraw(self, amount):
#         self.ammount= int(input("Enter ammount to withdraw: "))
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Ammount After withdraw: ",self.__balance)
#         else:
#             print("Insufficient balance")

# BankAccount = BankAccount()
# BankAccount.deposit(1000)


# class Student:
#     def __init__(self, name, marks):
#         self.__name = name
#         self.__marks = marks

#     def display(self):
#         print("Name:", self.__name)
#         print("Marks:", self.__marks)

# Student = Student("Khan",23)
# Student.display()


# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def update_salary(self, salary):
#         self.__salary = int(input("Enter new salary: "))

#     def display_salary(self):
#         print("Salary:", self.__salary)

# Employee = Employee(10000)
# Employee.update_salary(10000)
# Employee.display_salary()

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)


# Vehicle = Car("Toyota", "Corolla")
# Vehicle.display()

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def display(self):
#         print("Name:", self.__name)
#         print("Age:", self.__age)

# Person = Person("Khan", 30)
# Person.display()

# class Grandparent:
#     def __init__(self, family_name):
#         self.family_name = family_name

# class Parent(Grandparent):
#     pass

# class Child(Parent):
#     def display(self):
#         print("Family Name:", self.family_name)

# Child = Child("Khan")
# Child.display()


# class Device:
#     def __init__(self, brand):
#         self.brand = brand

# class Computer(Device):
#     pass

# class Laptop(Computer):
#     def display(self):
#         print("Laptop Brand:", self.brand)


# Laptop = Laptop("Dell")
# Laptop.display()


# class Person:
#     def __init__(self, name):
#         self.name = name

# class Employee(Person):
#     pass

# class Manager(Employee):
#     def display(self):
#         print("Manager Name:", self.name)

# object = Manager("Khan")
# object.display()


# class Academics:
#     subject = "CS"

# class Sports:
#     sport = "Cricket"

# class Student(Academics, Sports):
#     def show(self):
#         print(self.subject)
#         print(self.sport)


# object = Student()
# object.show()

# class Camera:
#     camera = "HD Camera"


# class MusicPlayer:
#     music = "MP3 Player"


# class Smartphone(Camera, MusicPlayer):
#     def show(self):
#         print(self.camera)
#         print(self.music)


# object = Smartphone()
# object.show()