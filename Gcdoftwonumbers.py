def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD of", num1, "and", num2, "is:", find_gcd(num1, num2))