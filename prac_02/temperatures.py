"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
William Hunter
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            calculate_celsius()
        elif choice == "F":
            calculate_fahrenheit()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def calculate_celsius():
    """converts Fahrenheit to Celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (5 / 9) * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")

def calculate_fahrenheit():
    """Converts Celsius to Fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

main()