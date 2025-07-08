# Recursion:

# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function that calls itself. 
# This has the benefit of meaning that you can loop through data to reach the result.

# We should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, 
# or one that uses excess amounts of memory or processor power. 
# However, when written correctly recursion can be very efficient and mathematically-elegant approach to progamming

# Cases:
# It has two cases:
# Base case - It runs until the base case is satisfied.
# recursive case - It continues the function until the total recursive cases are completed.

# Example:
# Recursion example:
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)  # Recursion step
        print(result)  # Print intermediate results
        return result  # Ensure the result is returned
    else:
        return 0  # Base case should return 0, not print its

print('Recursion example results:')
tri_recursion(4)



# Example-1:
# Printing the factorial of a number:

def factorial(n):
    if n == 0:      # It is the base case.
        return 1
    else:
        return n * factorial(n - 1)  # It is the recursive case.

print(factorial(5))


# Example-2:
# Printing fibonacci series using recursive function:

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(4))


# Example-3:
# fibonacci series upto to a given number using recursive function.

num = int(input('enter the number of series:' ))
def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
for i in range(num):
    print(fib(i),end=' ')


