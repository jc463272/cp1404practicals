""" William Hunter
CP1404
Answer all following questions
"""

#1 Write code that asked the user for their name and then opens a file called name.txt and writes that name to it.

out_file = open("name.txt", 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

#2 In the same file but as if it were a separate program write a code that opens "name.txt"
# and reads the name and prints the output

in_file = open("name.txt", 'r')

print(f"Hi {in_file.read().strip('\n')}!")
in_file.close()

#3 Create a text file called numbers.txt.
# write code that opens numbers.txt, read only the first two numbers, adds them together then prints result

with open("numbers.txt",'r') as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
print(number_1 + number_2)

#4 Now write a fourth block which print for all lines in numbers.txt
total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
