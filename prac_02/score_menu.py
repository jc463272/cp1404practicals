"""
William Hunter
"""

MENU = "(G)et valid score,(P)rint Result, (S)how stars, (Q)uit"


def main():
    """User menu"""
    score = 0
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            if score is not None:
                print_stars(score)
        else:
            print("Invalid score")
        print(MENU)
        choice = input(">>>").upper()
    print("Farewell")


def get_valid_score():
    """Prompt user for valid score"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def print_result(score):
    """print result of score"""
    result = determine_result(score)
    print(f"Your score is: {score}, your result: {result}")


def determine_result(score):
    """Determine result from score"""
    if score < 0 or score > 100:
        return "Invalid Score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    return "Excellent"


def print_stars(score):
    """print stars length of score"""
    print("*" * score)

main()
