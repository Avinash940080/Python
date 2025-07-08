# Membership operators are used to test whether value is a member of sequence, such as string, tuple, or set.
# There are two membership operators in python.

'''
in operator - Returns true if the value is found in the specified sequence.

not in operator - Returns True if the value is not found in the specified sequence.

'''

#Example

a = ['apple','banana','mango']
b = 'apple'
c = 'guava'

print(b in a) #Returns true as the given value is in the sequence.
print(c in a) #Similarily it returns false

a = ['apple', 'banana', 'mango']
b = 'guava'
c = 'apple'

print(b not in a) #Returns true as the given value is not in the sequence.
print(c not in a) #Similarily it returns false.