"""control statments let you control the flow of excution in your programs.
control structeres block of code runs,depending on conditions.
AS: if,else,elif,nested etc..

Identation:
python uses identation (spaces or tabs) to define block-level structures  instedad of curly
braces{} (like in c,c++,java).

convention: 4 spaces per indentation level/ 1 tab only.

example:
in case of other programming:
if(x>3){
print('x i sgreater than")}

Incase of python--->
if conitions:
#indented block runs if condition is True
"""
#1. simple if statments
"""
definition : executes a block of code only if the conditoons are true.

syntax :
if condition 
    # statemnts

 purpose:
 to perform an action when a condition is met.

"""
#examples:
"""
#1.check tempearture
temp = 32
if temp > 30:
    print('it is a hot')

#2.check bank balance
balance = 1000    
if balance >=500:
    print('sufficient funds')

#3.check driving age 
age = 20
if age >=18:
    print('you can drive')    

#4.door sensor
door_open = True
if door_open:
    print('door is open')    

#5.rain check
is_raining = False
if not is_raining:
    print("you don't  need an umbrella")    

#6.admin check 
user_role = 'admin'
if user_role == 'admin':
    print('access granted')

#7 high score 
score = 95
if score > 95:
    print('you got high score')

#8.room tempearture
room_temp = 25
if room_temp <30:
    print('room temperature is comforatable')

#9.morning check 
hour = 7
if hour <12:
    print('good morning !')

#10.stock price 
stock_price = 120
if stock_price > 100:
    print('stock price is above target')

"""

#====================================================================
#2.if-else statement:
"""
Definition:
excutes one block if conditions is true,otherwise excutes anthor block.

syntax:
if conditions:
    #true block
else:
    #false block

#purpose:
# to handle two mutually exclusive outcomes.    
"""

#1.pass/fail
marks = 45
if marks >=40:
    print('pass')
else:
    print('fail')    

#2.login success
username  = 'user'
if username =='admin':
    print('welocme ,admin 1') 
else:
    print('unknowm user') 

#3.light switch
light_on = False   
if light_on:
    print('light is on') 
else:
    print('light is off')

#4.attendance 
present = True
if present:
    print('marked present')
else:
    print('absent')

 #5.battery level
Battery = 10
if Battery < 20:
    print('low batter')  

else:
    print('battery is ok') 

#6.exam eligibility
attentandance_percentage = 80
if attentandance_percentage >=75:
    print('eligible for exam')
else:
    print('you are not eligible')

#7.payment status
payemnt_done = True
if payemnt_done:
    print('payment successful')
else:
    print('payment pending')

#8.seats availability
seats = 0
if seats > 0:
    print('seats available')
else:
    print('sold out')

 #9.discount offer
purchase_amount = 300
if purchase_amount <=300:
    print('discount appled')     
else:
    print('no discount') 

#10.file existence
file_exists = False
if file_exists:
    print('file found')   
else:
    print('file not found')      

#===============================================================
# 3.elif (else if) statements
"""
Defintion:
allows checking multiple sequently after an initial if.

syntax:
if condition1:
   #block1
elif condition2:
    #block
elif condition3:
    #block
else:
    #default block

purpose :
To handle multiple possible outcomes with clear priority.       
"""     
#example:

# 1. greetinhg based on time   
time = 18
if time < 12:
    print('good morning')
elif time < 17:
    print('good afternoon')        

else:
    print('good night')

#2.grade system:
marks = 65
if marks >90:
    print('A grade')
elif marks >=75:
    print('B grade')
elif marks >=60:
    print('C grade')
else:
    print('D grade') 

#3.WEATHER MESSAGE
temp = 5      
if temp >30:
    print('hot')
elif temp <=25:
    print('warm')             
else:
    print('cool')    

#4.bmi category:
bmi = 28
if bmi < 18.5:
    print('underweight')
elif bmi <25:
    print('normal weight')
elif bmi < 30:
    print('over weight')
else:
    print('obese')

#5.Membership level:
points = 300
if points >=1000:
    print('platinum member')
elif points >=500:
    print('gold member')
else:
    print('silver member')

#6.traffic light
signal = 'yellow'
if signal =='red':
    print('stop')
elif signal =='green':
    print('start')
else:
    print('get ready')  

#7. season finder 
month = 4
if month in  [12,1,2] :
    print('winter')                             
elif month in [3,4,5]:
    print('spring')
elif month in [6,7,8]:
    print('summer')
else:
    print('autumn')

#8.shipping cost
weight = 15
if weight <= 5:
    print('low shipping cost')
elif weight <=10:
    print('medium shipping cost')
else:
    print('high shipping cost')

#9.exam result
percentage = 55
if percentage <=85:
    print('excellent')
elif percentage >=75:
    print('very good')
elif percentage >=40:
    print('avearge') 
else:
    print('poor')   

#10.internet speed
speed = 50
if speed >=100:
    print('ultra fast internet')
            
elif speed >=50:
    print('fast internet')
else:
    print('slow internet') 

#4.NESTED STATEMNET:  
"""
 Definition:
  placing an if statement inside another if block.

  syntax:
  if outer_condition:
      if inner_condition
          #nested block
          purpose:
          To check multiple releated conditions hirerarchically.
"""     
#example:

#1.Job Eligibility
age = 25
degree = "bachelor"
if age >=18:
    if degree == "bachelor":
        print('eligible for job')

#2.purchase decision
price = 800
budget = 1000
if budget >=price:
    if price > 500:
        print('purchase with discount')
    else:
        print('puechase without discount')

#3. exam pass with grace
marks = 38
if marks < 40:
    if marks >35:
        print('pass with grace marks')
    else:
        print('fail')

#4. file operations:
file_open = True
file_type = 'text'
if file_open:
    if file_type == 'text':
        print('read text file')
    else:
        print('unsupported file type')

#5. security check
is_logged_in = True
is_admin = True
if is_logged_in:
    if is_admin:
        print('admin panel access')
    else:
        print('not access')                          
#6. car start 
key_in_ignition = True
fuel_available = True
if key_in_ignition:
    if fuel_available:
        print('car started')
    else:
        print('refuel needed')

#7. online calss attendance 
is_student_logged = True
class_active = True
if is_student_logged:
    if class_active:
        print('attend class')
    else:
        print('not attend the class')

#8. ATM withdrawal
card_inserted = True
pin_correct = False
if card_inserted:
    if pin_correct:
        print('withdrawal allowed')
    else:
        print('incorrect pin')

#9. game play
logged_in = True
has_subscription = False
if logged_in:
    if has_subscription:
        print('paly premium games')
    else:
        print('play free games')    
                    
#10. voting eligibility 
age = 20
citizen = True
if age >=18:
    if citizen:
        print('eligible to vote')
    else:
        print('citizenship required')    








