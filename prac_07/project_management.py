"""
Estimate:1.5 hrs
Actual:
"""

from project import Project
import datetime

FILENAME = "projects.txt"

def main():
    """Main menu to drive program."""
    print("Welcome to Project Management Program:")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} from {FILENAME}")
    display_menu()
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == 'L':
            load_projects(FILENAME)
        elif choice == 'S':
            save_projects(FILENAME, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects(projects)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            pass #update project
        else:
            print("Please enter a valid choice.")
        display_menu()
        choice = input(">>>").upper()

def display_menu():
    """Display menu options."""
    print("- (L)oad projects\n"
          "- (S)ave projects\n"
          "- (D)isplay projects\n"
          "- (F)ilter projects by date\n"
          "- (A)dd new project\n"
          "- (U)pdate project\n"
          "- (Q)uit")

def load_projects(filename):
    """Load projects from file."""
    projects = []
    with open(filename, "r", encoding="utf-8") as infile:
        infile.readline()
        for line in infile:
            parts = line.strip().split("\t")
            projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, "w", encoding="utf-8") as outfile:
        for project in projects:
            print(f"{project.name}, start: {project.start_date}, priority: {project.priority}, "
                  f"completion: {project.completion_percentage}%", file=outfile)

def display_projects(projects):
    """Display projects as complete or incomplete."""
    complete = [complete_project for complete_project in projects if complete_project.is_complete()]
    incomplete = [incomplete_project for incomplete_project in projects if not incomplete_project.is_complete()]
    print("Incomplete projects:")
    for incomplete_project in incomplete:
        print(f" \t{incomplete_project}")
    print("Complete projects: ")
    for complete_project in complete:
        print(f" \t{complete_project}")

def filter_projects(projects):
    pass

def add_project(projects):
    pass

def update_project(projects):
    pass

if __name__ == "__main__":
    main()



