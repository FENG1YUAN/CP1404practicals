"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

print Welcome to the Sales Bonus Program.
get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 0.10
    else
        bonus = sales * 0.15
    print The bonus is: bonus
    get sales
print Program ended.

"""


UNDER_THRESHOLD_BONUS = 0.10
OVER_THRESHOLD_BONUS = 0.15
SALES_THRESHOLD = 1000.0

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < SALES_THRESHOLD:
        bonus = sales * UNDER_THRESHOLD_BONUS
    else:
        bonus = sales * OVER_THRESHOLD_BONUS
    print(f"Bonus is: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))

print("Program ended")