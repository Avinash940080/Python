#calculator using arithmetic operators.

def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multipliply(x, y):
    return x*y
def divide(x, y):
    if y != 0:
        return x/y
    else:
        return "Error division by zero."

x = float(input('Enter the value of first number:'))
y = float(input('Enter the value of second number:'))

print("select the operation:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")


choice = input("Enter the choice (1/2/3/4): ")

if choice == '1':
    print(f'{x}+{y}={x+y}') 
elif choice == '2':
    print(x-y) 
elif choice == '3':
    print(x*y)
elif choice == '4':
    if y!=0:
        print(x/y)
    else:
        print("divison by zero is not defined.")
else:
    print("invalid input")
 







    