"""
William Hunter
"""

from random import randint

def main():
    """
    Prompt the user to enter a score, calculate and display the corresponding grade.
    Then generate a random score, calculate its grade, and display the result.
    """
    score = int(input("Score: "))
    result = determine_grade(score)
    random_score, random_result = get_random_grade()
    print(f"Your score is: {score}, your result: {result} ")
    print(f"Your score is: {random_score}, your result: {random_result} ")

def determine_grade(score):
    """Determine result from score"""
    if score < 0 or score > 100:
        return "Invalid Score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    return "Excellent"

def get_random_grade():
    """Give a random score and result between 0 and 100"""
    score = randint(0, 100)
    result = determine_grade(score)
    return score, result

main()
