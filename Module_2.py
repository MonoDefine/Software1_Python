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

numAverage = float(numProduct / 3)

print(f'Sum of numbers: {numSum}')
print(f'Product of numbers: {numProduct}')
print(f'Average of numbers: {numSum:.0f}')

# Task 5

# One talent is 20 pounds
# One pound is 32 lots
# One lot is 13.3 grams

# Convert to kilos and grams
