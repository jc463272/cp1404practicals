"""
William Hunter - CP1404
"""

COLOUR_TO_ASCII = {"absolute zero": "#0048ba", "acid green": "#b0bf1a",
                   "aliceblue": "f0f8ff", "alizarin crimson": "#e2636",
                   "amaranth": "#e52b50", "blond": "#faf0be",
                   "blue bell": "#a2a2d0", "british racing green": "#004225",
                   "charcoal": "#36454f", "citron": "#9fa91f"}

colour_name = input("Enter colour name: ")

while colour_name != "":
    if colour_name in COLOUR_TO_ASCII:
        print(f"The colour {colour_name} is: {COLOUR_TO_ASCII.get(colour_name)}")
    else:
        print(f"The colour {colour_name} is: N/A")
    colour_name = input("Enter colour name: ")
