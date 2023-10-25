"""
Software 1 - Python Module 7
Tuple, set, and dictionary
"""

# Task 1
seasons = ("spring", "summer", "autumn", "winter")

uInput = int(input("Provide the number of the month: "))

# Months 12 - 2 Winter, 3 - 5 Spring, 6 - 8 Summer, 9 - 11 Autumn

if uInput == 3 or uInput == 4 or uInput == 5:
    print(seasons[0])

elif uInput == 6 or uInput == 7 or uInput == 8:
    print(seasons[1])

elif uInput == 9 or uInput == 10 or uInput == 11:
    print(seasons[2])

elif uInput == 12 or uInput == 1 or uInput == 2:
    print(seasons[3])

else:
    print("Invalid month!")

# Task 2
nameSet = set()

while True:
    name = input("Provide a new name! ")

    if name == "":
        break

    if name in nameSet:
        print("Existing name")

    else:
        print("New name")
        nameSet.add(name)

for n in nameSet:
    print(n)

# Task 3
# Fetch and store the ICAO : Name of airports

airportDict = {}

while True:

    print("Choose an option: ")
    print("1. Register an Airport")
    print("2. Fetch Airport Information")
    print("3. Quit")

    uInput = input("")

    if uInput == "1":
        icao = input("Provide an ICAO code: ")
        name = input("Provide airport name: ")

        airportDict[icao] = name

    elif uInput == "2":
        fetch = input("Input ICAO code of airport: ")

        if fetch in airportDict:
            print(f"{fetch} : {airportDict[fetch]}")

    elif uInput == "3":
        print("Goodbye!")
        break
