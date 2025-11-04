
#🧱 SECTION A – BASIC PYTHON (Data Types, Operators, Input/Output)



#Q1. Create variables to store grocery item name, price, and quantity. Print all using formatted output.
grocery=['apple',300,2]
print(grocery)
#Q2. Calculate the total cost of 5 apples priced at ₹30 each using arithmetic operators.
apples=5
price=30
total=apples*price
print(total)
#Q3. Accept the user’s name and greet them with a welcome message to your grocery store.
name='sai'
user_name=f"{name} welcome to the grocery store:"
print(user_name)
#Q4. Check if a grocery item is available using a simple if-else condition.
grocery=['apple',300,2]
if grocery in apples:
    print(grocery)
else:
    print('not grocery items')    
#Q5. Convert the string "Rice" to uppercase and count the number of characters.
str='rice'
print(str.upper('rice'))
#Q6. Create a list of 5 grocery items and print the 2nd and 4th item.
grocery=[88,300,2,88]
print(grocery[0] and grocery[3])
#Q7. Add a new item to your grocery list and remove one old item.
a=grocery.append(2)
b=grocery.remove()
price(a)
price(b)
#Q8. Create a dictionary with grocery items as keys and prices as values. Print all pairs.
dict={'grocery_items':'apple','price':230}
price(dict.items())
#Q9. Use a comparison operator to check if the price of "Milk" > "Bread".
milk=21
bread=32
if 'milk' > 'bread':
    price('bread is greater then milk')
else:
    print('not greater')    
#Q10. Demonstrate logical operators to check if both "Milk" and "Eggs" are available.
list=['milk','bread']
if list in 'milk' and 'eggs':
    print('yes')
else:
    print('no')
#=======================================================================================================

#🔁 SECTION B – CONTROL STRUCTURES & LOOPS



#Q11. Take input of item quantity and print whether it is “In Stock” (>=10) or “Low Stock” (<10).
item=input('what is the qunatity you have :')
if item >=10 or item<10:
    price(item)
else:
    price('not stock you have',item)    
#Q12. Print all grocery items in your list using a for loop.
grocery=['apple',300,2]
for i in grocery:
    print(grocery)
  
#Q13. Display items with price greater than ₹50 using a for loop and if condition.
grocery=[32,30,2]
if grocery >50:
    price('is bigger')
#Q14. Use a while loop to simulate adding 5 items to a cart.

#Q15. Implement a discount system: if total > ₹500 → 10% discount, else → no discount.
num=600
if total > 500:
     print(num*10)
else :
    print('no discount.')
#Q16. Print numbers from 1 to 10 using range(), representing customer IDs.
for i in range(1,11):
    print(i)
#Q17. Create a multiplication table (1–10) for calculating price × quantity.for price in range(1, 11):
for quantity in range(1, 11):
    print(f"{price} x {quantity} = {price * quantity}")
print()  

#Q18. Find the most expensive item from a given dictionary using a loop.
items = {'apple': 50, 'banana': 30, 'milk': 60, 'bread': 40}

max_price = 0
expensive_item = ''

for item, price in items.items():
    if price > max_price:
        max_price = price
        expensive_item = item

print(f"The most expensive item is '{expensive_item}' with price ₹{max_price}")

#Q19. Print grocery items in reverse order using slicing or loop.
groceries = ['apple', 'banana', 'milk', 'bread', 'butter']
print(groceries[::-1])

#Q20. Create a nested loop to display the stock of 3 categories: Fruits, Vegetables, and Dairy.
stock = {
    'Fruits': ['Apple', 'Banana', 'Mango'],
    'Vegetables': ['Tomato', 'Potato', 'Carrot'],
    'Dairy': ['Milk', 'Cheese', 'Butter']
}

for category, items in stock.items():
    print(f"\nCategory: {category}")
    for item in items:
        print(f" - {item}")
#====================================================================================

#🧮 SECTION C – LOGIC BUILDING & PATTERNS



#Q21. Write a program to find the total and average bill amount of 5 customers.
total_bill = 0
customers = 5

for i in range(1, customers + 1):
    bill = float(input(f"Enter bill amount for customer {i}:"))
    total_bill += bill

average_bill = total_bill / customers

print("\n Bill Summary:")
print(f"Total bill amount = {total_bill}")
print(f"Average bill amount = {average_bill}")

#Q22. Generate a star pattern representing grocery shelves (rows = 5).
for i in range(1,6):
    print('grocery',end=" ")
       
#Q23. Display a pattern of item counts:
"""
1
1 2
1 2 3
1 2 3 4"""

for i in range(1,5):
    num=1
    for j in range(i):
        print(num,end=" ")
        num+=1
    print() 
   
  #
num=1
for i in range(1,5):

    for j in range(i):
        print(num,end=" ")
        num+=1
    print()      
#Q24. Find the 2nd highest priced grocery item without using built-in sort.
grocery = {'apple': 50, 'banana': 30, 'milk': 60, 'bread': 40, 'butter': 70}

highest = second_highest = 0
highest_item = second_item = ''

for item, price in grocery.items():
    if price > highest:
        second_highest = highest
        second_item = highest_item
        highest = price
        highest_item = item
    elif price > second_highest and price != highest:
        second_highest = price
        second_item = item

print(f"2nd highest priced item: {second_item} ({second_highest})")

#Q25. Write logic to combine two grocery dictionaries (merge items and add prices if duplicate).
grocery1 = {'apple': 50, 'banana': 30, 'milk': 60}
grocery2 = {'banana': 20, 'bread': 40, 'milk': 40}

merged = grocery1.copy()

for item, price in grocery2.items():
    if item in merged:
        merged[item] += price   # add prices if duplicate
    else:
        merged[item] = price

print("Merged Grocery List:")
for item, price in merged.items():
    print(f"{item}: {price}")

#=======================================================================================================

#🧰 SECTION D – FUNCTIONS (Built-in & User-defined)



#Q26. Use the built-in sum() to find the total cost of items in a list.
costs = [100, 250, 300, 150, 200]
total = sum(costs)
print(f"Total cost of items: ₹{total}")

#Q27. Define a function get_total(items) that takes a dictionary of item-price pairs and returns the total.
def get_total(items):
    return sum(items.values())

grocery = {'apple': 50, 'milk': 60, 'bread': 40}
print("Total price:", get_total(grocery))

#Q28. Create a function to calculate discount price using parameters price and discount_percent.
def discount_price(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount

print("Discounted price:", discount_price(500, 10))

#Q29. Define a function to find the cheapest item from a dictionary.
def find_cheapest_item(items):
    min_price = float('inf')
    cheapest = ''
    for item, price in items.items():
        if price < min_price:
            min_price = price
            cheapest = item
    return cheapest, min_price

grocery = {'apple': 50, 'banana': 30, 'milk': 60}
item, price = find_cheapest_item(grocery)
print(f"Cheapest item: {item} ({price})")


#Q30. Write a function that accepts a list and removes duplicates from it.
def remove_duplicates(items):
    return list(set(items))

grocery_list = ['apple', 'banana', 'apple', 'milk', 'banana']
print(remove_duplicates(grocery_list))

#Q31. Create a function search_item(item_name, grocery_list) that checks for item availability.
def search_item(item_name, grocery_list):
    if item_name in grocery_list:
        print(f"{item_name} is available ")
    else:
        print(f"{item_name} is not available ")

grocery = ['apple', 'banana', 'milk', 'bread']
search_item('milk', grocery)
search_item('butter', grocery)

#Q32. Define a recursive function to calculate factorial of quantity (for stock math).
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5 =", factorial(5))

#Q33. Use map() and lambda to increase each item’s price by 5%.
prices = [100, 200, 300, 400]
updated_prices = list(map(lambda x: x * 1.05, prices))
print("Updated prices (5% increase):", updated_prices)

#Q34. Use filter() and lambda to get all items costing more than ₹100.
prices = [80, 120, 60, 150, 200]
above_100 = list(filter(lambda x: x > 100, prices))
print("Items costing more than ₹100:", above_100)

#Q35. Use zip() to merge two lists — one with item names and one with prices — into a dictionary.
items = ['apple', 'banana', 'milk', 'bread']
prices = [50, 30, 60, 40]

grocery_dict = dict(zip(items, prices))
print("Merged grocery dictionary:", grocery_dict)
