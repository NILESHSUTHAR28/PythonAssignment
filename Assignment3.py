# Task 1:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter the number: "))

if num < 0:
    print("The factorial of negative number is 0")
else:
    result = factorial(num)
    print(f"Factorial of {num} is : {result}")



#Task 2 :
import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
natural_log = math.log(num)
sins_value = math.sin(num)


print(f"Square Root: {square_root}")
print(f"Natural Logarithm: {natural_log}")
print(f"Sins Value: {sins_value}")