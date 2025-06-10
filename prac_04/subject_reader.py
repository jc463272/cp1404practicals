"""
CP1404/CP5632 Practical
Data file -> lists program
William Hunter
"""

FILENAME = "subject_data.txt"


def main():
    """Read subjects and display"""
    subjects = load_subject()
    display_subjects(subjects)


def load_subject():
    """load data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(FILENAME,'r') as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
        return subjects

def display_subjects(subjects):
    """Display subjects"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students.")

main()