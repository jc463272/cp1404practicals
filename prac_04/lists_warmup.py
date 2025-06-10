"""CP1404 - William Hunter"""

numbers = [3, 1, 4, 1, 5, 9, 2]

#What is the output of the following and check in python console:

#numbers[0] => 3
#Correct

#numbers[-1] => 2
#Correct

#numbers[3] => 1
#Correct

#5 in numbers => True
#Correct

#7 in numbers => False
#Correct

#"3" in numbers => False
#Correct

#numbers + [6,5,3] => [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
#Correct

"""Write statements to achieve the following:"""

#1. Change the first element of the number to "ten"

numbers[0] = "ten"
print(numbers)

#2. change the last element to 1

numbers[-1] = 1
print(numbers)

#3. Print all the elements from the numbers except for the first two
numbers = numbers[2:]
print(numbers)

#4. Print whether 9 is an element of numbers
result = 9 in numbers
print(f"Is 9 in {numbers}: {result}")


