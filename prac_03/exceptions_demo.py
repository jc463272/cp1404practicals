"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

Answer: If the input received from user is not an integer data type.

2. When will a ZeroDivisionError occur?

Answer: The user inputs a zero value as the denominator of the division.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

 Answer: You could do so by checking the denominator input is valid before the division

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")