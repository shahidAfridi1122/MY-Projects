'''a = 5
b = 45
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")
isloggin = True
if isloggin:
    print("User is logged in")
else:
    print("User is not logged in")
isadmin = False
if isadmin:
    print("User is an admin")
else:
    print("User is not an admin")   
'''
weather = ["sunny", "rainy", "cloudy", "snowy"]
'''if weather[1] == "sunny":
    print("It's a sunny day")
elif weather[3] == "rainy":
    print("It's a rainy day")
elif weather[2] == "cloudy":
    print("It's a cloudy day")
elif weather[3] == "snowy":
    print("It's a snowy day")


if weather[0] == "sunny" and weather[2] == "rainy":
    print("It's a sunny and rainy day")

elif weather[0] == "sunny" or weather[3] == "rainy":

    print("It's a sunny day")
'''
sales = int(input("Enter your total sales:"))
salary = 10000
if sales > 1000 and sales <= 1500:
    total_salary = salary + (salary/100 * 20)
    print("Total salary with bonus:", total_salary)
    if sales >= 1500 and sales <= 2000:
        total_salary = salary + (salary/100 * 25)
        print("Total salary with bonus:", total_salary)
    else:
        sales > 2000 and sales <= 3000
        total_salary = salary + (salary/100 * 30)
    print("Total salary with bonus:", total_salary)
elif sales > 3000:
    total_salary = salary + (salary/100 * 40)
    print("Total salary with bonus:", total_salary)
