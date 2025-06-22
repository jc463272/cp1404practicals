"""
emails
estimate: 40 mins
actual: 30 mins
CP1404 - William Hunter
"""

def main():
    """Create a dictionary of emails"""
    email_to_name = {}
    email = input("Enter email: ")
    while email != "":
        name = return_name_from_email(email)
        confirmation = input(f"Is your name {return_name_from_email(email)}? (Y/n): ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Enter your name: ")
        email_to_name[email] = name
        email = input("Enter email: ")


    for name, email in email_to_name.items():
        print(f"{name} ({email})")

def return_name_from_email(email):
    """Extract name from email"""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name

main()
