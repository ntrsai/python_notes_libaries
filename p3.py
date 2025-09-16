#logical operators
#and ,or not
"""
age = 20
has_id = True
print(age >=18 and has_id)#True
print(age>=18 and has_id)#driving license

username = 'admin'
password = '123'
print (username == 'admin' or password == 'admin')#True

is_busy = True
print(not is_busy)#False

grade = 'A'
attendance = 90
print(grade == 'A' and attendance == 85)#False

income = 3000
credit_score = 750
print(income == 3000 and credit_score == 750)#True

height = 150
age = 12
print(height <= 150 and age <=10)#false

weight  = 80
age = 22
print(weight <=80 and age <=21)#true

total_amount = 400
coupons = True
print(total_amount > 50 or coupons )#true

msg = ''
print(not msg)#true if empty string 



is_weekend = True
is_holiday = False
print(is_weekend or is_holiday)#true  (dayoff ?)

#===========================
#biwsie opeartors -> &,^,<<,|,>>,~
#==========================


get binary operators
-------512,256,128,64,32,16,8,4,2,1
binary of 5 is 0101
binary of 3 is 0011

REAL LIFE APPLICATION : 
1.data  compression & storagfe optimization
use : bitwise  operators  help reduce  memeoru usage   by manipulating  bits directly.

2.image processing :
use : manipulating  pixels  value or apply  masks using  bitwise opeartors 

3.cryptography  &  security
use :simple encrypton  techniques  like xor  cipher  use bitwise opeartors

4.networking (ip subset masks):
use : bitwise opearations  are used to  calculate networks  adress and subnettings 

5.perforamances  optimizations (maths & game dev):
use : replace  multiplication/divison  with shifts  to optiminze  performance 


"""
a=5 #0101
b=3 #0011
print(a & b )#AND -> 1

a=5 #0101
b=3 #0011
print(a | b )#OR ->7

a=5 #0101
b=3 #0011
print(a ^ b )# XOR ->6

a=5 #0101
b=3 #0011
print(~a)#NOT ->-6

a=5 #0101
b=3 #0011
print(a >> b )# RIGHT SHIFT ->2

a=5 #0101
b=3 #0011
print(a <<b )# LEFT SHIFT ->40


x=7
mask = ~1
print(x & mask)

num= 4
print(num & 1 ==0)

#efficient calcualtions (swapping without  temp variables )

x = 10
y = 20 
x = x^y
y =  x^y
x = x^y
y =  x^y

"""
flags  and permission (access  control system)
imagine  managing user permisiion  like :
raed =1
write = 2
execute = 4

"""
#example  : assign  amd check  user access
#user red + excute 
"""
user_permission = 1 | 4 #5

#check if user has write access
has_write = user_permission & 2
print('write access',bool(has_write)) #false

#add write access
user_permission |=2
print('updated permission ',user_permission)

#========================
#membership opearators -> in , not in 
#========================

fruits = ['apple','grapes','pineapple']
print('apple' in fruits)#true
print( 'apple' not in fruits)#false

email = 'ntr@gmail.com'
print('@' in email)#valid email check

text = 'python  is powerfull'
print('python' in text)#true

username = ['test','admin']
print('admin' in username)

print('a' in 'data')

permission = 'rw'
print('r' in permission and 'w' in  permission)

banned = ['abc','xyz']
print('user1' not in banned)

courses = ['python','java']
print('python' in courses)

coupon_code = ['save50','new100']
print('save50' in coupon_code)

#=====================
#identity opearators -> is , not is 
#=================

a = [1,2,3]
b = a
c = [1,2,3]

print( a is b)
print(a is not b)
x = None
print( x is None)

print(id(a) == id(b))
  
x = 100
y = 100
print( x is y)


a.append(4)

s1 = 'hello'
s2 = 'heelo'
print(s1 is s2)

print(id(c))

b= [5,6]
print( 5 is b)

print( a==b )
print(a is c)


"""

#5.ESCAPE SEQUENCES
"""escape sequences are special characters specified proceeded by blackslash(/)used to represent
things are different  to type ,like a new linetabs,quotes,unicode characters.

"""
#1.new line --splitsoutput into the new line
print("hello\nworld")

#2.tab spaces


i=0
while True:

    print(i)

    if i>8:
       break
    i+=2