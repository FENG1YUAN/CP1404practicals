"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

get name
print (H)Hello
print (G)Goodbye
print (Q)Quit
get choice

while choice is not "Q"
    if choice is "H"
        print Hello, name
    else if choice is "G"
        print Goodbye, name
    else
        print Invalid choice

    print (H)Hello
    print (G)Goodbye
    print (Q)Quit
    get choice

print Finished.

"""


name = input("Enter name: ")

print("(H)Hello")
print("(G)Goodbye")
print("(Q)Quit")

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")

    print("(H)Hello")
    print("(G)Goodbye")
    print("(Q)Quit")

    choice = input(">>> ").upper()

print("Finished.")
