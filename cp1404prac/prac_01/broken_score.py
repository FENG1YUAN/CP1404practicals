"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

print Welcome to the Score Status Program.
get score
if score < 0 or score > 100
    print Invalid score
else if score >= 90
    print Excellent
else if score >= 50
    print Passable
else
    print Bad

"""


print("Welcome to the Score Status Program.")
score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")