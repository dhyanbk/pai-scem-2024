def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
fib_sequence = fibonacci(num_terms)
print(f"Fibonacci sequence: {fib_sequence}")