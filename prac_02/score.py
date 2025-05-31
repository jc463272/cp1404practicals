"""
CP1404/CP5632 - Practical
Broken program to determine score status
William Hunter
"""

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Incorrect score")
elif score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
else:
    print("Excellent")