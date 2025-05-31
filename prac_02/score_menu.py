"""
William Hunter
"""
from prac_02.score import determine_grade

MENU = "(G)et valid score,(P)rint Result, (S)how stars, (Q)uit"

def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Score: "))
        if choice == "P":
            determine_grade(score)
        if choice == "S":
            if score is not None:
                print_stars(score)
            else:
                print("Invalid score")
        else:
            print("Invalid choice")
    print("Farewell!")

def determine_grade(score):
    pass

def print_stars(score):
    print("*"*score)

main()
