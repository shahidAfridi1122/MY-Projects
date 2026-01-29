for i in range (1, 10):
    print (i*i)

text = input("Enter any String Values:")
count= 0
for ch in text.lower():
    if ch in "aeiou":
        count+=1
print("Number of wovels are: ",count)

marks= [23,43,63,67,43,85,33]
for i in marks:
    if i >=50:
        print(i)

i =1
while i <=20:
    if i % 2 !=0:
        print(i)
    i+=1


correct_password = "1234"
while True:
    password = input("Enter your Password:")
    if password == correct_password:
        print("Access Granted")
        break
    else:
        print("wrong password try Again.")

while True:
    data = input("Enter any sting: ")
    if data.lower()=="stop":
        print("program Turminated")
        break

n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total+=i
print("sum is: ",total)