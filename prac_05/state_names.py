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

length_of_code = max(len(code) for code in state_code_to_name.keys())

for code, name in state_code_to_name.items():
    print(f"{code:{length_of_code}} is \t{name}")

is_valid_state = False
while not is_valid_state:
    try:
        state = input("Enter state code: ").upper()
        if state in state_code_to_name:
            print(f"{state:{length_of_code}} is \t{state_code_to_name[state]}")
        elif state not in state_code_to_name:
            print("Invalid state code")
        else:
            is_valid_state = True
    except ValueError:
        print("Invalid short state")
    except TypeError:
        print("Invalid short state")

