

#More on If-Else, Elif, Nested Conditions

#1. Accept marks of 5 subjects and calculate total, percentage, and display division (First, Second, Third, Fail).
# #1
marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks of subject {i}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 60:
    print("Division: First")
elif percentage >= 45:
    print("Division: Second")
elif percentage >= 33:
    print("Division: Third")
else:
    print("Division: Fail")

#2. Accept temperature and display whether it is Hot, Moderate, or Cold.

temp = float(input("Enter temperature in °C: "))

if temp > 30:
    print("Hot")
elif temp >= 15:
    print("Moderate")
else:
    print("Cold")

#3. Accept a number and check whether it is Armstrong number or not (e.g., 153 = 1³+5³+3³).+========doubts==========================

#4. Accept a number and check whether it is a perfect number (sum of divisors = number).
# #4
num = int(input("Enter a number: "))

divisors_sum = sum(i for i in range(1, num) if num % i == 0)

if divisors_sum == num:
    print(num, "is a Perfect number ✅")
else:
    print(num, "is NOT a Perfect number ❌")

#5. Accept a character and check whether it is uppercase, lowercase, digit, or special symbol.
# #5
ch = input("Enter a single character: ")

if ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")

#6. Accept a string and check whether it is a palindrome string.
# #6
s = input("Enter a string: ").strip().lower()

if s == s[::-1]:
    print("Palindrome ✅")
else:
    print("Not Palindrome ❌")

"""7. Accept age and check the ticket price:
Age < 5 → Free
Age 5–12 → Rs 100
Age 13–59 → Rs 200
Age >=60 → Rs 150"""

"""8. Accept income from user and calculate tax as per given slabs:
Income ≤ 2,50,000 → No Tax
2,50,001–5,00,000 → 5%
5,00,001–10,00,000 → 20%
Above 10,00,000 → 30%"""


#10. Accept 3 numbers and check whether they can form a Pythagorean triplet (a²+b²=c²).

"""
Pass, Break, Continue (inside if-else & loops)

11. Print numbers from 1 to 10 but skip number 5 using continue.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

12. Print numbers from 1 to 10 but stop when number 7 comes using break.
for i in range(1, 11):
    if i == 7:
        break
    print(i)

13. Use a loop with pass inside if condition to demonstrate null statement.
for i in range(1, 6):
    if i == 3:
        pass   # nothing happens, loop continues
    print("Value:", i)

14. Accept a number and print whether it is prime or not, but break the loop if a factor is found.
n = int(input("Enter an integer: "))
if n <= 1:
    print(n, "is NOT prime")
else:
    is_prime = True
    import math
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            print("Not prime — factor found:", i)
            is_prime = False
            break   # stop searching further
    if is_prime:
        print(n, "is prime")

15. Accept 10 numbers from user and print only the positive numbers (skip negatives using continue).
positives = []
print("Enter 10 numbers:")
for _ in range(10):
    x = float(input())
    if x < 0:
        continue
    positives.append(x)

print("Positive numbers:", positives)

Nested If with Logic

16. Accept a number and check whether it is divisible by both 5 and 11.
n = int(input("Enter a number: "))
if n % 5 == 0 and n % 11 == 0:
    print(n, "is divisible by both 5 and 11")
else:
    print(n, "is NOT divisible by both 5 and 11")

17. Accept a string and check whether it contains both alphabets and digits.
s = input("Enter a string: ")
has_alpha = any(ch.isalpha() for ch in s)
has_digit = any(ch.isdigit() for ch in s)

if has_alpha and has_digit:
    print("String contains both letters and digits")
else:
    print("String does NOT contain both letters and digits")

18. Accept a number and check whether it is both a prime number and odd.#================doubts================================

19. Accept a year and check whether it is a century year (e.g., 1900, 2000).
year = int(input("Enter year: "))
if year % 100 == 0:
    print(year, "is a century year")
else:
    print(year, "is NOT a century year")

20. Accept two numbers and check whether the first is a multiple of the second.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b == 0:
    print("Cannot divide by zero")
elif a % b == 0:
    print(f"{a} is a multiple of {b}")
else:
    print(f"{a} is NOT a multiple of {b}")


Real-World Applications

21. ATM Program: Accept withdrawal amount and check conditions:
Amount multiple of 100
Minimum balance of 500 must remain
Deduct and display remaining balance.
balance = float(input("Enter current balance: ₹"))
withdraw = int(input("Enter withdrawal amount (multiple of 100): ₹"))

if withdraw % 100 != 0:
    print("Amount must be a multiple of 100")
elif balance - withdraw < 500:
    print("Transaction denied — minimum balance of ₹500 must remain")
else:
    balance -= withdraw
    print("Withdrawal successful. Remaining balance: ₹{:.2f}".format(balance))

22. Railway Ticket Discount: Accept age and class type (AC/General) → Provide discount:
Child (<12) → 50% off
Senior citizen (>=60) → 40% off
Otherwise → No discount
age = int(input("Enter age: "))
cls = input("Enter class (AC/General): ").strip().lower()
fare = float(input("Enter base fare: ₹"))

discount = 0
if age < 12:
    discount = 0.50   # 50%
elif age >= 60:
    discount = 0.40   # 40%
else:
    discount = 0.0

# Example: maybe AC has an additional fixed surcharge — but problem only asks discount
final = fare * (1 - discount)
print(f"Final fare after discount: ₹{final:.2f} (discount {discount*100:.0f}%)")

23. Cinema Hall Program: Accept movie type (Normal/3D/IMAX) and age → Show ticket price accordingly.
movie = input("Enter movie type (Normal/3D/IMAX): ").strip().lower()
age = int(input("Enter age: "))

# set base prices
prices = {"normal": 200, "3d": 350, "imax": 500}
price = prices.get(movie)

if price is None:
    print("Unknown movie type")
else:
    # example discount: children (<12) 50% off, senior (>=60) 30% off
    if age < 12:
        price *= 0.5
    elif age >= 60:
        price *= 0.7
    print(f"Ticket price: ₹{price:.2f}")

24. Online Shopping: Accept purchase amount →
= 5000 → 20% discount
= 2000 → 10% discount
Otherwise → No discount
amount = float(input("Enter purchase amount: ₹"))

if amount >= 5000:
    discount_rate = 0.20
elif amount >= 2000:
    discount_rate = 0.10
else:
    discount_rate = 0.0

final = amount * (1 - discount_rate)
print(f"Discount: {discount_rate*100:.0f}%, Final amount: ₹{final:.2f}")

25. Grading with Remark: Accept marks and display grade + remark 
(e.g., A → Excellent, B → Good, etc.).
"""
marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
else:
    if marks >= 90:
        grade, remark = "A+", "Excellent"
    elif marks >= 80:
        grade, remark = "A", "Very Good"
    elif marks >= 70:
        grade, remark = "B", "Good"
    elif marks >= 60:
        grade, remark = "C", "Fair"
    elif marks >= 50:
        grade, remark = "D", "Needs Improvement"
    else:
        grade, remark = "F", "Fail"

    print(f"Grade: {grade} — Remark: {remark}")
