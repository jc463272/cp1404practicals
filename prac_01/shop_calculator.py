"""
CP1404 - Shop Calculator
The program allows the user to enter the number of items and the price of each item.
Then the program computes and displays the total price of the items.
If the total price is over $100, then a 10% discount is applies to the total before the amount is displayed on the screen.
William Hunter
"""

total_price = 0

num_items = int(input("Enter number of items: "))

if num_items <= 0:
    print("No items entered")
else:
    for i in range(num_items):
        price = float(input("Enter price: "))
        while price < 0:
            print("Incorrect price")
            price = float(input("Enter price: "))
        total_price += price
    print(f"Total Price is {total_price}")

if total_price > 100:
    discount = total_price * 0.1
    discount_price = total_price - discount
    print (f"10% discount applied, the discounted price is now ${discount_price: .2f} ")


