

#Q1. Take two variables of number and character and concatenate it.
#(Example: yourname + birthdate → “Shalini1997”)
#answers:
name ='sai'
surname='keella'
print(name+surname)


#Q2. Take three variables. Example: emailid.
#(Store username, domain, extension separately and print complete email ID)
name ='sairaj'
email='saintrraj@gamil.com'
print(name,email)

#Q3. Take three variables and print your full name.
a='sai'
b='keella'
c=a+b
print(c)

#Q4. Find out the percentage of the student using input from users.
#(5 subjects, total marks = 500)
subject1=int(input("enter your biology subjects marks :"))
subject2=int(input("enter your maths subjects marks :"))
subject3=int(input("enter your telugu subjects marks :"))
subject4=int(input("enter your hindi subjects marks :"))
subject5=int(input("enter your science subjects marks :"))

total_subjects=subject1+subject2+subject3+subject4+subject5/500
print(total_subjects)
#Q5. Find out Area of Rectangle using user input.
#(length × breadth)

length=int(input("enter your area of rectangle length :"))
breadth=int(input("enter your area of rectangle breadth :"))
area_of_rectangle = length * breadth
print(area_of_rectangle)


#Q6. Find out Area of Square using user input.
#(side × side)

area_of_square_side_1=int(input("enter your area of square side :"))
area_of_square_side_2=int(input("enter your area of square side :"))
area_of_square = area_of_square_side_1* area_of_square_side_2
print(area_of_square)


#Q7. Find out Area of Circle using user input.
#(π × radius × radius)
area_of_circle_radius_1 =int(input("enter your area of circle radius :"))
area_of_circle_radius_2 =int(input("enter your area of circle radius :"))
area_of_circle=22/7*area_of_circle_radius_1*area_of_circle_radius_2
#Q8. Find out Perimeter of Rectangle.
#(2 × length + 2 × breadth)

length_1=int(input("enter your area of rectangle length :"))
breadth_2=int(input("enter your area of rectangle breadth :"))
perimeter_of_rectangle = 2 * length_1 +2 * breadth_2
print(perimeter_of_rectangle)

#Q9. Find out Perimeter of Square.
#(4 × side)
square_side =int(input("enter your perimeter of sqaure  :"))
perimeter_of_square = 4*square_side
print(perimeter_of_square)
#Q10. Find out Circumference of Circle.
#(2 × π × radius)
circle_radius=int(input("enter your Circumference of Circle :"))
Circumference_of_Circle = 2*22/7*circle_radius


#Q11. Find out Volume of Cube.
#(side × side × side)
side_1=int(input('enter your volume of cube side1:'))
side_2=int(input('enter your volume of cube side2:'))
side_3=int(input('enter your volume of cube side3:'))
volume_of_cube=side_1*side_2*side_3
print(volume_of_cube)

#Q12. Find out Volume of Cuboid.
#(length × breadth × height)
length=int(input("enter your volumn of cubiod length :"))
breadth=int(input("enter your volume of cubiod breadth :"))
height=int(input("enter your volumn of cubiod height :"))
volume_of_cubiod = length*breadth*height

#Q13. Find out Total Surface Area of Cube.
#(6 × side × side)
side_01=int(input('enter your surface area of cube side1:'))
side_02=int(input('enter your surface area of cube side2:'))
total_surface_area_of_cube=6*side_01*side_02
print(total_surface_area_of_cube)

#Q14. Find out Total Surface Area of Cuboid.
#(2(lb + bh + lh))


l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

# formula: 2(lb + bh + lh)
total_surface_area_of_cuboid= 2 * (l * b + b * h + l * h)

print("Total Surface Area of Cuboid:", total_surface_area_of_cuboid)


#Q15. Take a number from the user and check whether it is even or odd.
num=int(input('enter any number between 1-100 :'))
if num%2==0:
    print(num,'even number')
else:
    print(num,'odd numbers')    

#Q16. Take a number from the user and check whether it is positive, negative, or zero.

number=int(input('enter the any number :'))
if number >0:
    print('postive numbers')
elif number <0:
    print('negative numbers')    
else:
    print('zero')    


#Q17. Take marks of 3 subjects and find the average marks.

subjects_1=int(input("enter your biology subjects marks :"))
subjects_2=int(input("enter your maths subjects marks :"))
subjects_3=int(input("enter your telugu subjects marks :"))
average_marks=subjects_1+subjects_2+subjects_3/3
print(average_marks)

#Q18. Take temperature in Celsius from the user and convert it into Fahrenheit.
#(C×9/5)+32
celsius=int(input('enter a today temperature in celsius :'))
fahrenheit=celsius*9/5+32
print(fahrenheit)
#Q19. Take temperature in Fahrenheit from the user and convert it into Celsius.
#(F−32)×5/9
fahrenheit_1=int(input('enter a today temperature in celsius :'))
celsius_1=fahrenheit_1-32*5/9
print(celsius_1)

#Q20. Take principal, rate of interest, and time from the user and calculate Simple Interest.
#(P×R×T)/100
p=float(input("enter principal :"))
r=float(input("enter rate of interest :"))
t=float(input("enter time :"))
simple_interest=p*r*t/100
print(simple_interest)
#Q21. Take base and height from the user and find the area of a triangle.
#(1/2×base×height)
base=int(input('enter base:'))
height=int(input('enter height :'))
area_of_triangle_1=1/2*base*height
print(area_of_triangle_1)

#Q22. Take two numbers and find the maximum and minimum using Python functions.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum:", max(a, b))
print("Minimum:", min(a, b))

#Q23. Take a string from the user and find its length.
s = input("Enter a string: ")
print("Length of the string:", len(s))

#24. Take a string from the user and reverse it.---star:end:increment
s = input("Enter a string: ")
print("Reversed string:", s[::-1])

#Q25. Take a number from the user and print its square and cube.
# Q25
num = int(input("Enter a number: "))

print("Square:", num ** 2)
print("Cube:", num ** 3)
