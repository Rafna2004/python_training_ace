
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("--- Factorial Examples ---")
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of 7:", factorial(7))

print("\n--- User Input ---")
try:
    num = int(input("Enter a number: "))
    print(f"The factorial of {num} is: {factorial(num)}")
except ValueError:
    print("Please enter a valid integer.")
