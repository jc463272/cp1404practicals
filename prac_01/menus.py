"""
CP1404 - Menu
William Hunter
"""

name = input("Enter name: ")

print("(H)ello",sep = " ")
print("(G)oodbye",sep =" ")
print("(Q)uit", sep = " ")

choice = input(">>>")
while choice != 'Q':
    if choice == 'H':
        print(f"Hello, {name}!")
    elif choice == 'G':
        print(f"Goodbye, {name}!")
    else:
        print(f"Sorry, {name}! that is an invalid choice.")
    choice = input(">>>")
print("Finished")







