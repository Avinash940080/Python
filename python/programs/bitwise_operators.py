# Bitwise operators are used to compare two binary numbers.
# There are 6 types of operators.
'''
-AND(&) - sets each bit to 1, if both the bits are 1 or else 0.

-OR(|) - sets each bit to 1, if one of the bit is 1 or else 0.

-XOR(^) - sets each bit to 1, if only one of the bits is 1 or else 0.

-NOT(~) - inverts all the bits.

-left shift(<<) - Shifts the bits of the number to the left by specified number of positions.

-right shift(>>) - Shifts the bits of the number to the right by a specified number of positions.

'''

# Examples

# Bitwise AND(&):
a = 10
b = 5

print(a&b)
print(bin(a&b))


# Bitwise OR(|):
a = 10
b = 5

print(a|b)
print(bin(a|b))

# Bitwise XOR(^):
a = 10
b = 5

print(a^b)
print(bin(a^b))

# Bitwise NOT(~):
a = 10

print(~a)
print(bin(~a))
print(bin(a))

# Bitwise left shift(<<):
a = 10

print(3<<a)
print(bin(3<<a))

# Bitwise right shift(>>):
a = 10

print(3>>a)
print(bin(3>>a))



# Operators precedence is given by

'''
- paranthesis '()'
- Exponentiation '**'
- unary plus, unary minus, and bitwise NOT '+x','-x','~x'
- multiplication, division, floor division, and modulus '*','/','//','%'
- addition and subtraction '+','-'
- bitwise left and right shifts '<<','>>'
- bitwise AND '&'
- bitwise XOR '^'
- bitwise OR '|'
- all the comparison, identity and membership operators 
- Logical NOT 'not'
- Logical AND 'and'
- Logical OR 'or'

'''

