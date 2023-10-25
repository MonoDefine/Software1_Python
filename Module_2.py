# Software 1 - Python Module 2
# Variables and Interactive Systems

# Task 1
name = input(f'Hello, what is your name? \n')

print(f'Hello, {name}!')

# Task 2
import math

radius = int(input(f'Please provide a radius: \n'))

area = math.pi * (radius * radius)

print(f'The area of the circle is: {area}')

# Task 3
rectLength = int(input(f'Please provide length of the rectangle: \n'))

rectWidth = int(input(f'Please provide width of the rectangle: \n'))

rectArea = rectLength * rectWidth

print(f'Area of the rectangle is: {rectArea}')

# Task 4
numOne = int(input('Please input an integer: '))
numTwo = int(input('Enter another: '))
numThree = int(input('And another: '))

numSum = numOne + numTwo + numThree

numProduct = numOne * numTwo * numThree

numAverage = float(numSum / 3)

print(f'Sum of numbers: {numSum}')
print(f'Product of numbers: {numProduct}')
print(f'Average of numbers: {numAverage:.0f}')

# Task 5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_lots = (talents * 20 * 32) + (pounds * 32) + lots

total_grams = total_lots * 13.3

kilograms = total_grams // 1000

grams = total_grams - (kilograms * 1000)

print("The weight in modern units: ")
print(f"{kilograms:.0f}kg and {grams:.2f}g")

# Task 6
import random

three_digit = str(random.randint(0, 9))
three_digit += str(random.randint(0, 9))
three_digit += str(random.randint(0, 9))


print(f"Three Digit Code: {three_digit}")

four_digit = str(random.randint(1, 6))
four_digit += str(random.randint(1, 6))
four_digit += str(random.randint(1, 6))
four_digit += str(random.randint(1, 6))

print(f"Four Digit Code: {four_digit}")
