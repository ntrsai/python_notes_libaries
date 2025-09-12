"""a = 5
b = 5
sum = a*b
print(sum)"""

#single line comments .......it's not print the output only for expalining and highlighting the code 
"""multi line cooments """

"""
1.comment in python are denoted by the # symbol
2.any text after the # symbol on the same line is ignored  by the interpreter.
3.commnets are used to explain the code  and make it easier  to understand.
4.comments  cane be used to disable a block of code temporaily.
5.coemmnst can be used to documents the code ande make it easier  to understand  for other developers.

"""
# ------------------------------------------------------Session -2 ----------------------------------------------------------------

"""
1. What is Python Programming ?

Python is a high-level, interpreted, general-purpose programming language.
It was designed to be easy to read and write, making it ideal for beginners and professionals alike.
I Python is popular in web development, data science, automation, AI/ML, game development, and much more.
Real-Life Examples:
1. Instagram and YouTube use Python for backend.
2. Python scripts are used to automate Excel reports.

Real-life example :
1.Instagram and youtube use python for backend.
2.python scrpts are used to automate excel reports.
3.you can create chatbots,calculators,games and apps 

"""
"""
#using print() ->function
print('sai')
#print() used for messages printing/to dsiplay output
print("hello students ! welcome to python  session")
#print yor name
a = 'sai'
print('my name is :',a)
"""
"""
variables arec used to store data in python that can be used later,
it works as a container.
in python, you don't need to declare the type.
you can assign a value to a variable using the assignment operator (=).

RULES:

1.must start with a letter or underscore (ex:namw,_name)
2.can't start with a number (ex: 1name)
3.can include letters,digits ,underscores
4.can't include spaces or special characters
5.can't be a reserved keywords( ex: if,else,for ,while)

"""
"""
name = 'saikeella'
age = 21
city = 'Andhra pradesh'
print('my name is :',name)
print('my age is :',age)
print('my city is :',city)

print('my name is :',name ,' | my age is :',age,' | my city is :',city)

a = 5
b = 5
sum = a+b
print('sum :',sum)

#multiple by two numbers
a = 53
b = 98
print('sum :',a*b) 

#string conecnetation
first_name = 'sai'
last_name = 'keella'
full_name = first_name + last_name
full_name = first_name + " " + last_name
print(full_name)
"""
#print  informatio of my self
"""
name = 'saikeella'
age = 21
gender = 'male'
city = 'Andhra pradesh'
bank_balance = 2500
position = 'data analyst'

print('my name is :',name)
print('my age is :',age)
print('my gender is :',gender)
print('my city is :',city)
print('my bank balance  is :',bank_balance)
print('my position is :',position)

#using string concentataion
a = 'hello'
b = 'world'
c = a +" "+ b
print(c)"""
"""
# print multiple sentences together ( \n escape sequences used for new lines)
print(" hello students welcome to our python sesssion-2\nThis is the first session")

#srting concetation
print('hello wolrd' +" "+ "my self sai")
"""
#keywords
"""
Keywords are reserved words that have a special meaning in Python. 
They cannot be used as variable names.

Examples:
False, True, None, if, else, elif, while, 
for, break, continue, def, return, import, 
as, class, try, except

"""

# Using some keywords in a program
#is_Married = True
#print(is_Married)
"""
name = 'vicky'
is_Married = False
print(is_Married)
""" 

"""
Statements & Comments -->

Statements-->
Instructions that Python can execute.

Comments-->
Used to explain the code. They are ignored by the Python interpreter.

Single-line: starts with #

Multi-line: enclosed in ''' or """


# This is a single-line comment

name = "sai"  # storring name
print(name)

"""
7. Python Character Set

Character set refers to all the valid characters Python understands, including:

1. Letters – A to Z, a to z
2. Digits – 0 to 9
3. Special Symbols – + - * / = () {} [] etc.
4. Whitespace – space, tab, newline
5. Other Characters – Unicode characters
"""

#  to execute a selected part in python file --> select code --> Shift + Enter

# Using letters, digits, special characters
"""
a = 10        # digit
b = 20
sum = a + b   # using + operator
print("Sum:", sum)


#Example 4: Input Age and Print Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible yet.")



#Example 5: Calculate Area of a Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle =", area)

"""
age = int(input('enter you age :'))

if age >=18:
    print('you can eligible for vote')

else:
    print(
        'you are not eligible yet.')        

