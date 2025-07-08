#casting or typecast is considered as the conversion of one datatype to another datatype.

#converting to integers
my_float = 10.5
my_int = int(my_float)
print(my_int)

#converting to float
my_int = 10
my_float = float(my_int)
print(my_float)

#converting to string
my_float = 56.65
my_string = str(my_float)
print(my_string)


#converting to comlex numbers
my_int = -6
complex = complex(my_int)
print(complex)

#converting to boolean
my_string = 'hello'
Bool = bool(my_string)
print(Bool) #returns true for all the non empty variables and non '0' values.
#some of the examples of the truthy values are:

# non-zero number (e.g., 1, -1, 42, 3.14)
# Non-empty strings (e.g., "Hello", " ")
# Non-empty lists (e.g., [1, 2, 3], ["a", "b"])
# Non-empty dictionaries (e.g., {"key": "value"})
# Non-empty tuples (e.g., (1, 2, 3))
# Non-empty sets (e.g., {1, 2, 3})
# Non-empty frozensets (e.g., frozenset([1, 2, 3]))
# True


my_string = ''
boolean = bool(my_string)
print(boolean) #returns false all the empty variables and '0' values.

#some of the examples of the falsy values are

# None
# False
# 0 (zero)
# 0.0 (zero as a float)
# "" (empty string)
# [] (empty list)
# {} (empty dictionary)
# () (empty tuple)
# set() (empty set)
# frozenset() (empty frozenset)