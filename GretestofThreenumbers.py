def greatest_of_three(a, b, c):
    return max(a, b, c)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print("Greatest of the three numbers:", greatest_of_three(num1, num2, num3))