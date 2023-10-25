"""
Software 1 - Python Module 5
List structures and iterative loops (for)
"""

# Task 1
import random


x = 0
u_num = int(input("Enter how many dice to roll: "))

for n in range(1, u_num + 1):
    die_roll = random.randint(1, 6)
    x += die_roll

print(x)

# Task 2
number = []
while True:
    u_input = (input("Give a number: "))
    if u_input == "":
        break
    u_input = int(u_input)

    number.append(u_input)

number.sort(reverse=True)
for n in range(0, 5):
    print(number[n])

