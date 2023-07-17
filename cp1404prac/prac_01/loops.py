"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

for i in range 1 to 21 with step 2
    print i without line break
print line break

for i in range 0 to 101 with step 10
    print i without line break
print line break

for i in range 20 to 1 with step -1
    print i without line break
print line break

get n
for i in range 1 to n+1
    print '*' without line break
print line break

for i in range 1 to n+1
    print '*' i times

"""


for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

n = int(input("Number of stars: "))
for _ in range(n):
    print('*', end='')
print()

for i in range(1, n+1):
    print('*' * i)
