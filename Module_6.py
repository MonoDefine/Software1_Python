"""
Software 1 - Python Module 6
Functions
"""

# Task 1 + 2
import random


# Function that returns a number between 1 and the limit
def die_roller(limit):
    result = random.randint(1, limit)

    return result


value = 0

uInput = int(input("What number-sided die do you wish to roll? "))

while value < uInput:
    value = die_roller(uInput)
    print(value)


# Task 3
# Function which returns gallons to liters calculation
def gallons_to_liters(gal):
    liters = gal * 3.785
    return liters


amount = 0

while True:
    uInput = int(input("Provide amount of gas in gallons: "))

    if uInput >= 0:
        amount = gallons_to_liters(uInput)
        print(f"{uInput} gallons is {amount} liters")

    else:
        print("Closing program!")
        break


# Task 4
def lst_sum(lst):
    return sum(lst)


lst = []

while True:
    uInput = int((input("Provide a number to the list: ")))

    lst.append(uInput)

    uCont = input("Continue? (N to break) ").upper()

    if uCont == "N":
        break

print(f"Value is: {lst_sum(lst)}")


# Task 5
# Function returns a parameter list with odd numbers removed
def lst_evener(lst):
    for num in lst:
        if (num % 2) != 0:
            lst.remove(num)
    return lst


lst = []

while True:
    uInput = int((input("Provide a number to the list: ")))

    lst.append(uInput)

    uCont = input("Continue? (N to break) ").upper()

    if uCont == "N":
        break

lst = lst_evener(lst)

for n in lst:
    print(n)

# Task 6
import math

# Function requests for diameter of a pizza
def p_diameter(num):
    diam = float(input(f"Provide the diameter of pizza {num} in cm: "))

    return diam

# Funtion requests the price of a pizza
def p_price(num):
    price = float(input(f"Provide the price of pizza {num} in €: "))

    return price

# Function calculates the price per square centimeters
def pizza_calculator(diam, price):
    area = math.pi * (diam**2)
    value = price / area
    return value


pOne = pizza_calculator(p_diameter(1), p_price(1))

pTwo = pizza_calculator(p_diameter(2), p_price(2))

if pOne < pTwo:
    print("Pizza One has more value than Pizza Two!")
    print(f"P1: {pOne:.2f}€/cm2 vs P2: {pTwo:.2f}€/cm2")

elif pOne > pTwo:
    print("Pizza Two has more value than Pizza One!")
    print(f"P1: {pOne:.2f}€/cm2 vs P2: {pTwo:.2f}€/cm2")

else:
    print("Both pizzas share the same value!")
    print(f"P1: {pOne:.2f}€/cm2 vs P2: {pTwo:.2f}€/cm2")

