#-------------------------------------loops staments------------------------------------

#loops are used to excute a block of code repeatedly for a specified number of times.
"""
num1=1
num2=2
num3=3
num4=4
num5=5
#using for loop  to print numbers from  1 to 5
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)

#using 'FOR' loop to print numbers from 1 to 5
#range 
for i in range(1,6):
    print(i)

"""
"""
1.while loop -->
the while loop continues excuting a block as long  as the conditions is true

syntax:
while condition 
    #block of code


#Examples:

# examples 1: print numbers from 1 to 5
i = 1           #start
while i <= 5:   #conditions
    print(i)
    i+=1         #incremnet

#example 2: print even numbers less then 10
num = 2
while num < 10:
    print(num)
    num+=1    
  
#example 3: print sum of numbers till 100
total = 0
i = 1
while i <=100:
    total +=i
    i+=1
    print('total',total)

#example 4: countdown timer
count = 5
while count > 0:
    print(count)
    count -=1

#example 5: validating user input
user_input = " "
while user_input !='yes':
    user_input = input("type  'yes' to continue :")

"""
"""
2.simulated do-while loop (python doesn't have built-in -do while)
A do-while loop excute the block at least once and then checks the conditons.

syntax: simulted using while true and break

"""    
#examples:
"""
#example 1: print number once ,then check 
i = 1
while True:
    print(i)
    if i >=5:
        break
    i+=1

#example 2: user password input validation
while True:
    password = input('enter password:')
    if password == 'admin':
        print('access granted')  
    else:
        print('incorrect password :')   

#example 3: menu simulation
while True:
    print("1. start\n2. exist")
    choice = input('enter choice :')
    if choice == '2':
        break
#example 4: sum input until 0
while True:
    num = int(input('enter number (0 to stop):'))   
    if num == 0:
        break

#example 5 : print even number till 10
i= 0
while True:
    i +=2
    print(i)
    if i > 10:
        break

"""
"""
for loop --> A for loop is ued tio iterate over a sequence (like list,tuple,string)
syntax:
for variable in sequence:
    #block
"""
"""
#examples:
#example 1: print numbers 1 to 5
for i in range(1,6):
    print(i)

#example 2: print characters in a string
for char in 'python':
    print(char)    
#example 3: sum of numbers using for loop 
total = 0   
for i in range(101):
    total +=i
print('sum:',total)
#example 4: print table of 3
for i in range(1,11):
    print('3 x',i,"=",3*i) 
#example 5: countdown from 5
for i in range(5,0,-1):
    print(i)      

"""
#4. for loop when iterating over collections
"""    
for i in range(101):
    if i%2==0:
        print('even',i)
    else:
        print('odd',i)    

#example 1: list items
fruits=["apple","banana","cheery"]
for i in fruits:
    print(i)

#example 2: dictionary keys and values

person = {"name":"john","age":21}
#for i in person.items():
   # print(i) 
for key,value in person.items():
    print(key,":",value) 

#example 3: set elements
colors = {"red","blue",'green'}
for i in colors:   
    print(i)   

#example 4:tuple itera=tion
nums=(10,20,30)
for i in num:
    print(num)

#example:5 iterating over string
for i in "hello":
    print(i)    
"""
#5.nested loops
#A loop inside  another loop .useful for grids ,patterns a,matrics ,etc

"""
#example 1: print matrix

for i in range(3):#rows 
    for j in range(3):#columns
        print(i,j)
    print()#empty line for better readibility

#example 2: multiplication table
for i in range(1,4):
    for j in range(1,4):
        print(f"{i}x{j}={i*j}",end="\t")
    print()    

#example: 3 star patteren

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()       

#example :4 number grid

for i in range(4):
    for j in range(4):
        print("*",end="")
    print()  

#example 5: nested list processing

matrix =[[1,2],[3,4],[5,6]]  
for row in matrix:
    for col in row:
        print(col)   
    print()          

#6.break statemnts  
# break is used to exit the loop prematurely

#example  1: stop loop at 5

for i in range(11):
    
    if i==3:
        break
    print(i)#0,1,2

#example 2: while loop break

i=1
while True:
    if i >3:
        break
    print(i)
    i+=1
#example 3: loop user input until 'exit'

while True:
    a=input("type 'exit' to stop :")
    if a =='exit':
        break
#example 4:stop on negtaive nukmbers

num2=[1,2,-1,4]   
for i in num2:
    if i <0:
        break
    print(i) 

#example: 5 break in nested loop

for i in range(3):
    for j in range(3):
        if j==2:
            break
        print(i,j)

#7.continue statments

#continue skips theb currents loop iterartion and movies to teh next one.

#example 1: skip even numbers

for i in range(1,6):
    if i %2==0:
        continue
    print(i)

#example 2: skip specific items

names = ['john'," ",'mike']
for i in names:
    if names == " ":
        continue
    print(i)    

#example:3 skip on condition

for i in range(1,6):
    if i ==3:
        continue
    print('number',i)  

#example 4: skip zero division

nums =[1,0,2]
for i in nums:
    if i ==0:
        continue 
    print(i)     

#example 5: continue in while loop

i=0
while i<5:
    i+=1
    if i==3:
        continue
    print(i)
    """
#8.else with loops
    
    #else in loop runs only if the loop complete normally (no breaks)

    #example 1: simple for -else
for i in range(5):
    print(i)
else:
    print('loop complted')

    #example 2: break prevents else
for i in range(5):
    if i ==3:
        break
    print()
else:
    print('will not print')    

    #example 3: while-else
for item in [1,2,3]:
    x=0
    while x<3:
        print(x)
else:
    print('while finished') 

    #example 4:search success check
for item in [1,2,3]:  
    if item ==4:
        print('found')
else:print('not found')
     #example 5: no break ,so else runs
for i in [10,20,30]:    
    print(i)
else:
    print('loop done')
                 


#9 infinite loop
#a loop that never ends unless broken manually
#example 1: basic infinite loop
while True:
    print('running....')
    break
#example 2: menu system
while True:
    print('1.show\n.exist')
    if input('choice:') == '2':
        break
#example 3: server ping simulation
while True:
    print('pinging server')
    break #simulate stop    
#example 4: countdown until stop
while True:
    stop=input('stop ? (yes):')
    if stop == 'yes':
        break
#example 5 : retry until corect
while True:
    code = input('enter your code')
    if code =='1234':
        print('correct') 
        break
"""
10.list/dict comprehension (loop shortcuts)
comprehensions offer a short syntax for loops inside losts,sets, and dicts.

"""  
#example 1: squares list
squares =[x**2 for  x in range(5)]
print(squares)

# Example 2: Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Example 3: Dictionary comprehension
sqr_dict = {x: x**2 for x in range(3)}
print(sqr_dict)

# Example 4: String to char list
chars = [ch for ch in "Data"]
print(chars)

# Example 5: Filter names
names = ["Ram", "Raj", "Rani"]
r_names = [name for name in names if name.startswith("R")]    
print(names)