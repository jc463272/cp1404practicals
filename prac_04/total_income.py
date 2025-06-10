"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
William Hunter
"""


def main():
    """Display income report given number of months."""
    number_of_months = int(input("How many number_of_months? "))
    incomes = get_incomes(number_of_months)
    report = generate_report(incomes)
    display_report(report)

def get_incomes(number_of_months):
    """Calculate the accumulative monthly income"""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}:"))
        incomes.append(income)
    return incomes

def generate_report(incomes):
    """Generates report of monthly incomes"""
    total = 0
    lines = []
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        lines.append((month, income, total))
    return lines

def display_report(lines):
    """Displays report based on incomes"""
    print("\nIncome Report\n-------------")
    for month, income, total in lines:
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()
