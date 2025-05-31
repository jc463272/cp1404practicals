"""
William Hunter
CP1404
"""

def main():
    """Print stars same length as password"""
    get_password()

def get_password():
    password = input("Password: ")

    while len(password) <= 5:
        print("Password must be greater than 5 characters long")
        password = input("Password: ")

    print('*'*len(password))

main()