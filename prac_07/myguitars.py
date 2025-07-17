"""
Estimated: 20 mins
Actual:
"""

from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Main program to load the guitars and store new guitars into a list."""
    guitars = load_guitars(FILENAME)
    print(f"The following guitars were loaded from {FILENAME}: ")
    guitars.sort() #Sort the list of guitars by year before they are displayed
    display_guitars(guitars)


def load_guitars(filename):
    """Load the guitars data from a csv file."""
    guitars = []
    with open(filename,'r', encoding="utf-8") as infile:
        for line in infile:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0],int(parts[1]),float(parts[2])))
    return guitars


def display_guitars(guitars):
    """Display formatted guitars data."""
    for i, guitar in enumerate(guitars):
        print(f"{i+1}. {guitar}")

if __name__ == "__main__":
    main()
