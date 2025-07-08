#logical operators are used to combine conditional statements.
#logical operators in python are:

'''
and - It returns true if both the statements are true.
or  - It returns true if one of the statements is true.
not - It reverses the result, if the statement is true then it returns false and vice versa.

'''

#Examples

a = int(input('enter the value of a:'))
b = int(input('enter the value of b:'))
c = int(input('enter the value of c:'))

# Logical 'and' operator
print(a>b and b>c)

#logical 'or' operator
print(a>b or b>c)

#logical 'not' operator
print(not (a>b and b>c))