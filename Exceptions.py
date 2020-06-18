def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("You can't divide by 0")
        return "Infinity"


while True:
    try:
        num1 = int(input("Please insert the first number: "))
        num2 = int(input("Please insert the second number: "))
        break
    except ValueError:
        print("Wrong values, please try again")

print(f"The result of {num1}/{num2} =", str(division(num1, num2)))


def division2():
    try:
        num1 = float(input("Please insert the first number: "))
        num2 = float(input("Please insert the second number: "))
        print(f"The result of {num1}/{num2} =", str(division(num1, num2)))
    except ValueError:
        print("Wrong values, please try again")
    except ZeroDivisionError:
        print("You can't divide by 0")


division2()

import math


def sqrtNumber(num1):
    if num1 < 0:
        raise ValueError("The number can't be a negative one")
    else:
        return math.sqrt(num1)


num1 = int(input("Please insert the number: "))

try:
    print(sqrtNumber(num1))
except ValueError as negativeNumber:
    print("Negative Number")
