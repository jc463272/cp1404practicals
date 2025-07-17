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
    display_guitars(guitars)

    guitars += get_new_guitar() #add new guitar to list
    guitars.sort()

    print(f"The following guitars were added to {FILENAME}:")
    display_guitars(guitars)
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load the guitars data from a csv file."""
    guitars = []
    with open(filename,'r', encoding="utf-8") as infile:
        for line in infile:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0],int(parts[1]),float(parts[2])))
        guitars.sort()
    return guitars


def display_guitars(guitars):
    """Display formatted guitars data."""
    for i, guitar in enumerate(guitars):
        print(f"{i+1}. {guitar}")

def get_new_guitar():
    """Get new guitar from user."""
    guitars = []
    print("Enter new guitar")
    name = input("Enter name: ")
    if name != "":
        year = input("Enter year: ")
        cost = input("Enter cost: ")
        guitars.append(Guitar(name,int(year),float(cost)))
        name = input("Enter name: ")
    return guitars

def save_guitars(filename, guitars):
    """Save the guitars data into a csv file."""
    with open(filename,'w', encoding="utf-8") as outfile:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}",file=outfile)


if __name__ == "__main__":
    main()
