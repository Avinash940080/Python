# Python Tuples:
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written in round brackets '()'.

# Example:
my_tuple = ('apple', 'banana', 'mango')
print(my_tuple)

# Tuples allow duplicate values.
# Tuples are unchangeable.
# Items in tuple have a defined order and that order will not change.

# Example
my_tuple = ('apple', 'banana', 'mango', 'banana')
print(my_tuple)
print(my_tuple[0])


# Tuple length:
# To determine how many times a tuple has, use 'len()' function:

# Example
my_tuple = ('apple', 'banana', 'mango')
print(len(my_tuple))

# Creating a tuple with one item 
# To create a tuple with only one item, you have to add comma after the item, otherwise Python will not recognize it as a tuple.

# Example
my_tuple = ('apple',) # It is recognized as a tuple.
my_tuple = ('apple')  # It is not recogized as a tuple.

print(my_tuple)


# Tuple items - Data Types
# The items can be of any datatypes

# Example:
tuple1 = (1, 2, 5, 7, 8)  # integer items
tuple2 = ('what', 'is', 'this') # string items
tuple3 = (True, False, True, False) # boolean items

print(tuple1)
print(tuple2)
print(tuple3)

# A single tuple can contain different datatypes.

# Example:
my_tuple = ('apple', 'banana', 'mango', 1, 2, 5, 6, True, False, False)
print(my_tuple)


# type()
# python identifies the type as 'tuple'

# Example
my_tuple = ('apple', 'banana', 'mango')
print(type(my_tuple))


# The tuple() Constructor
# It is used to convert a given data into tuple

# Example:

('apple', 'banana', 'mango')
my_tuple = tuple(('apple', 'banana', 'mango')) # note the double rounded brackets
print(my_tuple)



# Access tuple items:
# We can access tuple items by referring to the index number, inside square brackets.

# Example:
my_tuple = ('apple', 'banana', 'mango')
print(my_tuple[0]) # Prints the first item in the tuple.

# negative indexing:
# We can also access items in the tuple by negative indexing starting from -1.
# It starts from the end of the tuple.

# Example:
my_tuple = ('apple', 'banana', 'mango')
print(my_tuple[-1]) # Prints the last item in the tuple.


# Range of indexes.
# We can specify a range indexes by specifying where to start and where to end.
# When specifying a range, the return value will be a new tuple with the specified items.

# Example:
my_tuple = ('apple', 'banana', 'mango', 'kiwi', 'orange')
print(my_tuple[0:3]) # start index 0 is included and end index 3 is not included.
print(my_tuple[0::]) # It prints every items starting from the given index no.(here '0')


# Range of negative indexes:
# It is similar to the above example but it starts from the end of tuple
# The index from the end starts from -1.

# Example
my_tuple = ('apple', 'banana', 'mango', 'kiwi', 'orange')
print(my_tuple[-4:-1]) # start index -4 is included and end index -1 is not included.
print(my_tuple[-4::])  # It prints every items starting from the given index no.(here '-4')


# Check if Item Exists:
# To determine if a specified item is present in a tuple use the 'in' keyword.

# Example:
my_tuple = ('apple', 'banana', 'mango', 'kiwi', 'orange')

if 'kiwi' in my_tuple:
    print('YES')
else:
    print('NO')



# Python - Update Tuples:
# Tuples are immutable (i.e we can't change the update or change the values once the tuple is created).
# But there are ways to do these operations. They are:

# Add items to a tuple:

# 1 - convert the given tuple into a list and append the items into the list , then convert it back to tuple again.
# Example:
my_tuple = ('apple', 'banana', 'mango', 'kiwi', 'orange')
my_list = list(my_tuple)
print(my_list)
my_list.append('guava')
my_tuple = tuple(my_list)
print(my_tuple)


# 2 - Add one to tuple to another tuple.
# Example:
my_tuple = ('apple', 'banana', 'mango', 'kiwi', 'orange')
tuple_1 = ('guava',)

my_tuple += tuple_1
print(my_tuple)



# Remove Items in a tuple:
# convert the tuple into a list, then remove it using 'remove()' method and convert it back to tuple.
# Example:
my_tuple = ('apple', 'banana', 'mango', 'kiwi', 'orange')
a = list(my_tuple)
print(a)
a.remove('kiwi')
my_tuple = tuple(a)
print(my_tuple)


# Deleting a tuple.
# We can delete the tuple completely using 'del' keyword.

# Example:
my_tuple = ('apple', 'banana', 'mango', 'kiwi', 'orange')
del my_tuple
# It throws an error if we print the tuple, as the given tuple has been deleted.