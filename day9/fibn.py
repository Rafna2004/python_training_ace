def fibonacci(n):
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def fibonacci_recursive(n):
   
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    num_terms = 10
    print(f"Fibonacci sequence with {num_terms} terms:")
    print(fibonacci(num_terms))

    print(f"\nThe 10th Fibonacci number (0-indexed 9th term): {fibonacci_recursive(9)}")
