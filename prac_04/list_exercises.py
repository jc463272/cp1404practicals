"""
CP1404 - William Hunter
Prompts user for 5 numbers output information of these numbers
"""

numbers = []

for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)
print(numbers)

print(f"the first number is: {numbers[0]}")
print(f"The last number is: {numbers[-1]}")
print(f"the smallest number is: {min(numbers)}")
print(f"the largest number is: {max(numbers)}")
print(f"the average number is: {sum(numbers)/len(numbers):.2f}")

#Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter a username: ")

if username in usernames:
    print(f"Access granted!")
else:
    print(f"Access denied!")
