""""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese
"""

while True:
    try:
        kilograms = float(input('Enter your weight :'))
        if kilograms > 0:
            break
        else:
            print("Please try again.")
    except ValueError:
        print("Invalid kilograms")


while True:
    try:
        height = float(input('Enter your height :'))
        if height > 0:
            height = height / 100
            break
        else:
            print("Please try again.")
    except ValueError:
        print("Invalid height") 

bmi = kilograms / (height ** 2)

if bmi >= 30.0:
    print('Obese')
elif bmi >= 25.0:
    print('Overweight')
elif bmi >= 18.5:
    print('Normal weight')
else:
    print('Underweight')


print(f'Your weight : {kilograms:.2f}')
print(f'Yoyr height : {height:.2f}')
print(f'Your Bmi is : {bmi:.2f}')