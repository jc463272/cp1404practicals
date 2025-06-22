"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_CODE_TO_NAME = {"QLD": "Queensland",
                      "NSW": "New South Wales",
                      "NT": "Northern Territory",
                      "WA": "Western Australia",
                      "ACT": "Australian Capital Territory",
                      "VIC": "Victoria",
                      "TAS": "Tasmania",
                      "SA": "South Australia"}

length_of_code = max(len(code) for code in STATE_CODE_TO_NAME)

for code, name in STATE_CODE_TO_NAME.items():
    print(f"{code:{length_of_code}} is {name}")

is_valid_state = False
while not is_valid_state:
    try:
        state = input("Enter state code: ").upper()
        if state in STATE_CODE_TO_NAME:
            print(f"{state:{length_of_code}} is \t{STATE_CODE_TO_NAME[state]}")
        elif state not in STATE_CODE_TO_NAME:
            print("Invalid state code")
        else:
            is_valid_state = True
    except TypeError:
        print("Invalid short state")
