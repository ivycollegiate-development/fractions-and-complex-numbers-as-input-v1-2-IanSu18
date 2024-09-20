from fractions import Fraction 
try:
    num1 = Fraction(input("Please enter a fraction number (ex:3/4): "))
    print(num1)
except ZeroDivisionError:
    print("Invalid opperation, You cannot divide by zero")
except ValueError
    print("Invalid response, Please input a functional value")