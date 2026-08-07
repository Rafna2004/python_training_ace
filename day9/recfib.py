def fibonacci_recursive(n):
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def print_fibonacci_series(terms):
   
    print(f"Fibonacci series up to {terms} terms:")
    series = [fibonacci_recursive(i) for i in range(terms)]
    print(series)

if __name__ == "__main__":
    n_terms = 10
    print_fibonacci_series(n_terms)
