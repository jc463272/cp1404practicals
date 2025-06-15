"""
CP1404 - William Hunter
Write a program that asks the user for number of quick picks.
Generates lines of output which consists of 6 random number between 1 and 45
"""

from random import randint

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Generate number of picks and display them"""
    number_of_picks = get_valid_picks()
    all_quick_picks = generate_quick_picks(number_of_picks)
    display_quick_picks(all_quick_picks)


def get_valid_picks():
    """Prompt the user for a valid number of picks."""
    is_finished = False
    while not is_finished:
        try:
            number = int(input("Enter number of picks: "))
            if number < 0:
                raise ValueError("Number must be positive integer")
            is_finished = True
        except ValueError:
            print("Invalid input. Try again.")
    return number  # No problem with undefined variable


def generate_quick_picks(number_of_quick_picks):
    """Generates list of quick picks with unique numbers between 1 and 45."""
    all_quick_picks = []
    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(NUMBERS_PER_LINE):
            number = randint(MINIMUM, MAXIMUM)
            while number in all_quick_picks:
                number = randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()
        all_quick_picks.append(quick_picks)
    return all_quick_picks


def display_quick_picks(quick_picks):
    """Display all quick picks in aligned format."""
    for quick_pick in quick_picks:
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
