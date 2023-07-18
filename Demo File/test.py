def fibonacci(n):
    if n <= 0:
        print("Invalid input. N must be a positive integer.")
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage
n = int(input("Enter the value of N: "))
result = fibonacci(n)
if result is not None:
    print(f"The {n}th term in the Fibonacci series is: {result}")



