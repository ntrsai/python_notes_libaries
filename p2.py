#example 1 : calculate  total marks of students.subjects :hindi,english,maths,pysics,histroy,arts
"""
student_name = input('enter your name :')
marks_hindi = float(input('enter your hindi marks:'))
marks_english = float(input('enter your english marks:'))
marks_maths = float(input('enter your maths marks:'))
marks_physics = float(input('enter your physics marks:'))
marks_histroy = float(input('enter your histroy marks:'))
marks_arts = float(input('enter your arts marks:'))

total_marks_score = marks_hindi + marks_english + marks_maths + marks_physics + marks_histroy + marks_arts
print('total marks ',student_name,'is :',total_marks_score)


#remember  to use  int()  or float()  when you're working with numbers.
#the input( )functions always  treturns a string ,so you  need to  convert it  to a number  if 
#you want  to perform  mathematical operations on it.


#without conversion
a = input('enter your number :')#string
b = input('enter your number :')
total = a + b #adds
print('total marks is :',total)


#with conversion
num1 = int(input('enter your number :')) #integer
num2 = int(input('enter your number :'))
total_num = num1 + num2 # adds
print('total number is :',total_num)


# Greet the user
#input() is used to take input from the user
name = input("Enter your name: ")
print(f"Welcome, {name}!") # f-string used to include variable in string
age = input("Enter your age: ")
print(f"Your age is {age}") # f-string used to include variable in string

address = input('enter your address :')
print(f'your address is {address}')
"""
#===============================================================================
# VARIABLES
# A variable is a named container to store data.
# Python is dynamically typed. No need to declare data types.
# Syntax:
# variable_name = value
name =123
name="hello"
# Examples:
name = "Shalini"
age = 28
city = "Mumbai"
fees = 5000.75
is_available = True
temperature = 37.5
mobile = "9876543210"
email = "shalini@example.com"
grade = 'A'
distance_km = 12.3
#..........................
#DATA TYPES
#-------------------------
"""
Python has various built-in data types to handle different kinds of data. Here are some common ones
Python supports the following data types:
Python supports the following data types:
1. int             - Integer (e.g., 10)
2. float           - Decimal numbers (e.g., 5.67)
3. str             - Text data (e.g., "hello")
4. bool            - Boolean (True/False)
5. list           - Ordered, changeable, allows duplicates
6. tuple           - Ordered, unchangeable, allows duplicates
7. set             - Unordered, no duplicates
8. dict            - Key-value pairs
9. NoneType        - Represents no value


"""
#---------------------
#real world example:
#--------------------
units =10 #int
price = 10.9 #float
product = 'laptop'#string
is_active = True #boolean
items =['pen','book'] #list
dimension =(20,13)#tuple
unique_id = {102,109}#set
student = {'name': 'sai','age ':21}#dictionary
data = None #Nonetype
#type checking
print(type(price)) #output : <class : 'float'>

#===========================
#operators in python 
#==========================
"""
operators are used to perform operations  on variables and  values.
types:
1.Arthemtical operators 
2.Relational(comparsion)
3.assignment
4.logical
5.bitwise
6.membership 
7.identify


"""
#==========================
#1.Arthmetical opertors : +,-, /,%,*,//,**
a= 15
b = 3
print(a+b)#addition :18
print(a-b)#subtract :12
print(a*b)#multiplication :45
print(a/b)#divison :5.0
print(a**b)#exponents :3375
print(a%b)#modulus :0
print(a // b)#floor divsion like remainder :5

#real-life
price = 50
quantity = 20
print('total :',price * quantity)
 
marks = 50
marks1 = 20 
print('total',marks + marks1 / 3)

second =250
print('minutes',second // 60)

age = 18
print(age >=18)#True

marks =45
print(marks >=45)#tRUE

amount =9999
print(amount < 10000)#true

entered_pin =1234
real_pin = 4321
print(entered_pin == real_pin)#False

temp =25
print(temp !=30)#true

height =154
print(height > 150)#true

weight = 65
print(weight <=70)#true

name = 'sai'
print(name == 'sai')#true

price = 200
print(price >=100 and price <=500)#true

num = 6
print(num %2==0)#true

#===============================
#2.assignment operators - (%=, +=,-=,*=,/=,//=,**=)


x = 10
x += 5
x-= 3
x *= 2
x /= 4
x %= 4


#Use case:
salary = 10000
salary += 2000 # 12000

steps = 1000
steps += 500
total = 0

item_price = 250
total += item_price

lives = 3
lives -=1

wallet = 1000
wallet -= 250
