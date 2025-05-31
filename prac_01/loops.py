"""
CP1404 - Practising Loops
Willian Hunter
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

""" a. Count in 10s from 0 to 100"""

for j in range(0,110,10):
    print(j, end=' ')
print()

"""b. count down from 20 to 1"""
for k in range(20,0,-1):
    print(k, end=' ')
print()

"""c. print n in stars. Ask the user for a number, then print that many stars, all in one line"""

num_stars = int(input("Enter number of stars: "))

for n in range(num_stars):
    print('*', end=' ')
    print()
print("------------")

"""d. print n lines of increasing stars"""
num_stars = int(input("Enter number of stars: "))

for s in range(num_stars + 1):
    print('*'* s, sep=' ')
    print()