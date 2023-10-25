"""
Software 1 - Python Module 3
Conditional Structures
"""

# Task 1
zndLength = float(input("Provide the length of your zander (cm): "))

if zndLength >= 42:
    print("That's a good fish!")

else:
    amountBelow = 42 - zndLength
    print(f"Sorry, your zander is {amountBelow}cm below the size limit.")
    print("Throw it back!")

# Task 2
luxDesc = 'LUX: upper-deck cabin with a balcony.'
aDesc= 'A: above the car deck, equipped with a window.'
bDesc = 'B: windowless cabin above the car deck.'
cDesc = 'C: windowless cabin below the car deck.'


print("Hello user! Choose a cabin class to enter.")
print(luxDesc)
print(aDesc)
print(bDesc)
print(cDesc)

uInput = input('').upper()

if uInput == 'LUX':
    print('You have chosen cabin LUX. Welcome aboard!')

elif uInput == 'A':
    print('You have chosen cabin A. Welcome aboard!')

elif uInput == 'B':
    print('You have chosen cabin B. Welcome aboard!')

elif uInput == 'C':
    print('You have chosen cabin C. Welcome aboard!')

else:
    print("Invalid cabin class.")

# Task 3
uGender = input("Provide your biological gender (M / F): ").upper()
uHemoglob = int(input("Provide your hemoglobin value (g/l): "))

if uGender == 'M':
    if uHemoglob >= 167:
        print("Your hemoglobin level is high.")
    elif uHemoglob <= 134:
        print("Your hemoglobin level is low.")
    else:
        print("Your hemoglobin level is normal.")
elif uGender == 'F':
    if uHemoglob >= 155:
        print("Your hemoglobin level is high.")
    elif uHemoglob <= 117:
        print("Your hemoglobin level is low.")
    else:
        print("Your hemoglobin level is normal.")
else:
    print("Invalid input! Try again.")

# Task 4

