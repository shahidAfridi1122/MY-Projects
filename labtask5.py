'''class car:
    model = 1999 
    color = "red"
    print(model , color)
obj=car()


class rectangle:
    length = 12
    width = 2
    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width) 
obj1 = rectangle()
print("Area is:",obj1.area())
print("Perameter are:",obj1.perimeter())



class student:
    def __init__(self,name, eng , maths, urdu):
        self.name= name
        self.eng= eng
        self.maths = maths
        self.urdu = urdu
    def average(self):
        return (self.maths+self.urdu+self.eng)/3
obj2 = student("Shahid Khan",34,56,65)
print("Average is: ",obj2.average())

class student:
    def __init__(self,marks):
        self.marks= marks

    def result(self):
        if self.marks>33:
            return "pass"
        else:
            return "fail"

obj3 = student(34)
print(obj3.result())


class account:
    def __init__(self , balance , account_number):
        self.balance = balance
        self.account_number = account_number

    def calculate(self):
        self.op =input("select option: ")
        if self.op == "1":
            self.balance= self.balance + int(input("Enter amount to deposit: "))
        elif self.op == "2":
            self.balance = self.balance - int(input("Enter amount to withdraw: "))
            if self.balance < 0:
                print("Insufficient balance")
        elif self.op == "3":
            print("Your balance is: ", self.balance)
        else:
            print("Invalid option selected")
    
obj4 = account(1000, 123456)
obj4.calculate()

'''
class employee:
    def __init__(self,id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        annual_salary = self.salary * 12
        print(f"Employee ID: {self.id}, Name: {self.name}, Monthly Salary: {self.salary}, Annual Salary: {annual_salary}")

obj5 = employee(101, "Shahid Khan", 5000)
obj5.display()