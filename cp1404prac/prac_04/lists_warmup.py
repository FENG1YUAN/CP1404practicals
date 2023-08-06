"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

The code creates a list called numbers with specific integers.

Several operations are performed on the list, including indexing, slicing, and checking membership.
These operations print out certain elements of the list, subsets of the list,
and whether specific numbers or strings are present in the list.

The code also appends a list to the end of the numbers list and prints the result.

The first and last elements of the list are then modified, and the updated list is printed each time.

Finally, the code prints out all elements of the list excluding the first two,
and checks whether the number 9 is present in the list.
"""


numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])     # 3
print(numbers[-1])    # 2
print(numbers[3])     # 1
print(numbers[:-1])   # [3, 1, 4, 1, 5, 9]
print(numbers[3:4])   # [1]
print(5 in numbers)   # True
print(7 in numbers)   # False
print("3" in numbers)  # False
print(numbers + [6, 5, 3])  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
print(numbers)    # ['ten', 1, 4, 1, 5, 9, 2]

numbers[-1] = 1
print(numbers)    # ['ten', 1, 4, 1, 5, 9, 1]

print(numbers[2:])  # [4, 1, 5, 9, 1]

print(9 in numbers)  # True
