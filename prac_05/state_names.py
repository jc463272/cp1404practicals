"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

state_code_to_name = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania",
                "SA": "South Australia"}

state = input("Enter short state: ").upper()
while state != "":
    if state in state_code_to_name:
        print(state, "is", state_code_to_name[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
