radius=int(input("Enter the radius: "))
area = 2 * 3.14 * radius
print("Area is: ",area)
a = 5
b = 7
print("A befor Swap: ",a)
print("B befor Swap: ",b)
c =a 
a = b
b = c
print("A After Swap:",a)
print("B After Swap:",b)

celsius = int(input("Enter the Temperature in Celsius: "))
Fahrenheit= (celsius*9/5)+32
print("Temperature in Fahrenheit is: ",Fahrenheit)

marks=list(map(int,input("Enter the Five Subject Marks and Space is must After each marks: ",).split()))
total_marks= 500
obtain_marks= sum(marks) 
percentage = (obtain_marks/total_marks)*100
print("Total Marks are: ",obtain_marks)
print("Percentage is: ",percentage)

int_number = input("Enter an integer value:")
float_value = float(int_number)
float_number= float(input("Enter any float value:" ))
int_value = int(float_number)
print("Integer to Float: ",float_value)
print("Float to integer: ",int_value)


list1= [23,42,5,34,23]
total = sum(list1)
maximum = max(list1)
minimum = min(list1)
print("Sum is: ",total)
print("Maximum number in list is: ",maximum)
print("Minimum number in list is: ",minimum)

mylist = []
for i in range(5):
    a = int(input("Enter any number:"))
    mylist.append(a)
print("List is: ",mylist)

list2=[23,5,32,52]
print(list2)
list2.append(34)
print(list2)

list2.insert(3,467)
print(list2)

list2.remove(467)
print(list2)

list2.pop(2)
print(list2)