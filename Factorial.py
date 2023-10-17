def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
try:
    num = int(input("Enter a non-negative integer: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")
