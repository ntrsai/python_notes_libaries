

#1. Check whether a number is divisible by 7.
num=int(input('enter your numbers :'))
if num%7==0:
    print('divisble by 7',num)
else:
    print('not divisble by 7 :',num)
    
#2. Check whether a given number is even or odd.
num=int(input('enter your numbers :'))
if num%2==0:
    print('even numbers:',num)
else:
    print('odd numbers :',num)


#3. Check whether a given number is positive, negative, or zero.
num=int(input('enter your numbers :'))
if num>0:
    print('postive numbers :',num)
elif num<0:
    print('negative numbers:',num)    
else:
    print('zero',num)

#4. Check whether the character 'a' is present in the string "Python" or not.
a='python'
if 'a' in a:
    print('it is correct:',a)
else:
    print('incorrect',a)    


#5. Accept three numbers and find the largest number among them.
a=2
b=6
c=8
if a>b and a>c:
    print(a,'is greater')
elif b>a and b>c:
    print(b,'is greater')
elif c>a and c>b:
    print(c,'is greater')   
else:
    print('nothing ')     


#6. Check whether a given year is a leap year or not.
year =int(input('enter your birthday year :'))
if year%4==0:
    print('it is leap year',year)
else:
    print('it si not leap year',year)    

#7. Accept total working days and present days, calculate attendance percentage
#  and check eligibility for exams (>=75%).
working_days=365
present_days=float(input('enter your present days :'))
attendance=working_days/present_days*100

if attendance >= 75:
    print(" Eligible for exams")
else:
    print("Not Eligible for exams")

#8. Check whether the entered character is a vowel or not.
vowel='a'
if vowel.lower() in ['a','e','i','u','o','s']:
    print('you entered characters is a vowel',vowel)
else:
    print('not vowel',vowel)
#9. Accept a number from 1 to 7 and print the day of the week (1=Sunday, 2=Monday, …).
num=int(input('enter  a number from 1 to 7:'))
if num==1:
    print('sunday')
elif num==2:
    print('monday')  
elif num==3:
    print('tuesday')  
elif num==4:
    print('wednesday') 
elif num==5:
    print('thursda')  
elif num==6:
    print('friday')
elif num==7:
    print('satursday')    
else:
    print('re-try you enter a wrong number')    


#10. Accept a city name and display its monument.
#Delhi → Red Fort
#Agra → Taj Mahal
#Jaipur → Jal Mahal

city = input("Enter a city name : ")

if city == "Delhi":
    print("Monument: Red Fort")
elif city == "Agra":
    print("Monument: Taj Mahal")
elif city == "Jaipur":
    print("Monument: Jal Mahal")
else:
    print("Sorry, monument not found for this city.")



#11. Check whether a person is eligible to vote (age >=18).
age = 18
if age>=18:
    print('you are eligble  to vote:',age)
else:
    print('not eligble',age)
#12. Make a simple calculator (add, subtract, multiply, divide) using if-elif.
num1=int(input('enter a number :'))
num2=int(input('enter a number:'))
add=num1+num2
subtract=num1-num2
multiple=num1*num2
divide=num1/num2
if num1+num2:
    print('addition',add)
if num1-num2:
    print('addition',subtract)
if num1*num2:
    print('addition',multiple)
if num1/num2:
    print('addition',divide)   
else:
    print('your task is completed')             
#13. Check whether a figure is square or not by comparing length and breadth.

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

if length == breadth:
    print(" The figure is a Square")
else:
    print(" The figure is NOT a Square")


#14. Accept percentage from user and display grade:
#Below 25 → D
#325–45 → C
#45–50 → B
#50–60 → B+
#60–80 → A
#Above 80 → A+
# #14: percentage -> grade

    pct = float(input("Enter percentage (0-100): ").strip())
    if pct < 0 or pct > 100:
        print("Please enter a valid percentage between 0 and 100.")
    else:
        if pct < 25:
            grade = "D"
        elif pct < 45:   # 25-44.999...
            grade = "C"
        elif pct < 50:   # 45-49.999...
            grade = "B"
        elif pct < 60:   # 50-59.999...
            grade = "B+"
        elif pct < 80:   # 60-79.999...
            grade = "A"
        else:            # 80-100
            grade = "A+"
     


#15. Accept three sides of a triangle and check whether it is equilateral, isosceles, or scalene.
# #15: classify triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check validity first
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")

#16. Accept three sides of a triangle and check whether the triangle is valid (sum of any two sides > third side).
# #16: check triangle validity
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

is_valid = (a + b > c) and (a + c > b) and (b + c > a)
print("Triangle is valid:" if is_valid else "Triangle is NOT valid.")

#17. Check whether a key exists in a dictionary or not.
# #17: check key existence
d = {"name": "Sai", "age": 22, "city": "Pune"}  # example dictionary
key = input("Enter key to check: ").strip()

# Method 1: using 'in'
if key in d:
    print(f"Key '{key}' exists. Value = {d[key]}")
else:
    print(f"Key '{key}' does NOT exist.")


#18. Check whether a number is a three-digit number or not#--------------------doubts----------------
#19. Accept electricity units and calculate bill:
#First 100 units → Free
#Next 200 units → Rs 2/unit
#Above 300 units → Rs 5/unit
# #19: Electricity Bill Calculator

units = int(input("Enter electricity units consumed: "))

bill = 0

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 2
else:
    bill = (200 * 2) + (units - 300) * 5   

print(f"Total units: {units}")
print(f"Electricity Bill: ₹{bill}")

#Logical & Nested Structures

#20. Accept age, sex (M/F), number of working days, and calculate wages/day as per rules:
#Age 18–30: M → 700/day, F → 750/day
#Age 30–40: M → 800/day, F → 850/day
#Otherwise → Print “Enter appropriate age”
#
age = int(input("Enter age: "))
sex = input("Enter sex (M/F): ").strip().upper()
working_days = int(input("Enter number of working days: "))

wage_per_day = None

if age<=18  or age <= 30:
    wage_per_day = 700 if sex == "M" else 750 if sex == "F" else None
elif age<=31 or age <= 40:           
    wage_per_day = 800 if sex == "M" else 850 if sex == "F" else None
else:
    print("Enter appropriate age")

if wage_per_day is None:
    
    if 18 <= age <= 30 or 31 <= age <= 40:
        print("Invalid sex input. Use 'M' or 'F'.")
else:
    total = wage_per_day * working_days
    print(f"Wage per day: ₹{wage_per_day}")
    print(f"Total wage for {working_days} days: ₹{total}")

#21. Accept three numbers and display the second largest number.
# #21
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

numbers = [a, b, c]
numbers.sort()
second_largest = numbers[-2]
print("Second largest number is:", second_largest)

"""22. Accept number of days late for library book submission and calculate fine:
Up to 5 days → Rs 2/day
6–10 days → Rs 3/day
11–15 days → Rs 4/day
More than 15 days → Rs 5/day"""
# #22
days_late = int(input("Enter number of days late: "))

if days_late <= 0:
    fine = 0
elif days_late <= 5:
    fine = days_late * 2
elif days_late <= 10:
    fine = days_late * 3
elif days_late <= 15:
    fine = days_late * 4
else:
    fine = days_late * 5

print(f"Days late: {days_late}, Fine: ₹{fine}")


#23. Accept a number and check whether it is a prime number.#-----------------------doubts--------------------
# #23
n = int(input("Enter an integer: "))

if n <= 1:
    print(n, "is NOT prime")
else:
    is_prime = True
    import math
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(n, "is prime" if is_prime else "is NOT prime")


#24. Accept a number and check whether it is a palindrome number (same when reversed).
# #24
n = input("Enter a number: ").strip()
if n == n[::-1]:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is NOT a palindrome")


#25. Accept a string and check whether it is an anagram of another string (e.g., "care" → "race")
#=====================================doubts===============================================================