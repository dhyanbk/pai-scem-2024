def Fib(n):
    if n<= 0:
        print("Incorrect input")
    # First number is 0
    elif n == 1:
        return 0
    # Second number is 1
    elif n == 2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
 
n = int(input("Enter a number: "))
fib_value = Fib(n)
print(f"{n}th Fibonacci number is {fib_value}")