'''
Arithmetic Operators:

Addition: +
Subtraction: -
Multiplication: *
Division: /
Floor Division: //
Modulus: %
Exponentiation: **
Comparison Operators:

Equal to: ==
Not equal to: !=
Greater than: >
Less than: <
Greater than or equal to: >=
Less than or equal to: <=
Assignment Operators:

Assignment: =
Addition assignment: +=
Subtraction assignment: -=
Multiplication assignment: *=
Division assignment: /=
Floor division assignment: //=
Modulus assignment: %=
Exponentiation assignment: **=
Logical Operators:

Logical AND: and
Logical OR: or
Logical NOT: not
Identity Operators:

is: Returns true if both variables are the same object
is not: Returns true if both variables are not the same object
Membership Operators:

in: Returns true if a sequence with the specified value is present in the object
not in: Returns true if a sequence with the specified value is not present in the object
Bitwise Operators:

Bitwise AND: &
Bitwise OR: |
Bitwise XOR: ^
Bitwise NOT: ~
Left Shift: <<
Right Shift: >>
'''
# Arithmetic operators
a = 10
b = 5
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Comparison operators
x = 10
y = 20
print("\nComparison Operators:")
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)

# Logical operators
p = True
q = False
print("\nLogical Operators:")
print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)

# Bitwise operators
m = 10  # Binary: 1010
n = 7   # Binary: 0111
print("\nBitwise Operators:")
print("AND:", m & n)   # Result: 2 (Binary: 0010)
print("OR:", m | n)    # Result: 15 (Binary: 1111)
print("XOR:", m ^ n)   # Result: 13 (Binary: 1101)
print("NOT:", ~m)      # Result: -11 (Binary: 11110101, Two's complement)
print("Left Shift:", m << 1)  # Result: 20 (Binary: 10100)
print("Right Shift:", m >> 1) # Result: 5 (Binary: 101)

# Assignment operators
x = 5
print("\nAssignment Operators:")
x += 3  # Equivalent to: x = x + 3
print("+=:", x)
x -= 2  # Equivalent to: x = x - 2
print("-=:", x)
x *= 2  # Equivalent to: x = x * 2
print("*=:", x)
x /= 4  # Equivalent to: x = x / 4
print("/=:", x)

# Identity operators
a = [1, 2, 3]
b = [1, 2, 3]
print("\nIdentity Operators:")
print("Is:", a is b)      # False - Checks if both variables refer to the same object
print("Is not:", a is not b)  # True - Checks if both variables do not refer to the same object

# Membership operators
list1 = [1, 2, 3, 4, 5]
print("\nMembership Operators:")
print("In:", 2 in list1)      # True - Checks if the value exists in the sequence
print("Not in:", 6 not in list1)  # True - Checks if the value does not exist in the sequence
