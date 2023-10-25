"""
Software 1 - Python Module 4
While loops (while)
"""

# Task 1
x = 1

while x < 1001:
    x += 1

    if (x % 3) == 0:
        print(x)

# Task 2
while True:
    u_inches = int(input("Please provide a measurment in inches: "))
    if u_inches < 0:
        break
    else:
        print(f"{u_inches}in is {u_inches * 2.54}cm.")

# Task 3
temp = True
while True:
    u_num = input("Enter a new number! ")
    if u_num == "":
        break
    u_num = int(u_num)

    if temp:
        smol = u_num
        larg = u_num
        temp = False

    if u_num > larg:
        larg = u_num
    elif u_num < smol:
        smol = u_num

print(f"The smallest number was {smol} and the largest number was {larg}")

# Task 4
import random

lucky_num = random.randint(1, 10)

while True:
    u_guess = int(input("Guess a number, 1 to 10: "))

    if u_guess < lucky_num:
        print("Too low!")
    elif u_guess > lucky_num:
        print("Too high!")
    else:
        print(f"Good job! The number was {u_guess}.")
        break

# Task 5
username = "python"
password = "rules"
x = 0
while True:
    u_user = input("Username: ")
    u_pass = input("Password: ")

    if u_user == username and u_pass == password:
        print("Welcome")
        break
    else:
        print("Incorrect information.")
        x += 1

    if x == 5:
        print("Access Denied.")
        break

