
# Python - Unpack Tuples
# When we create a tuple, we normally assign values to it, This is called "packing" a tuple.
# Unpacking is a process in which the values in the tuples are extracted back into variables.


# Example1 - packing:
colors = ('black', 'blue', 'green', 'red')
print(colors)

# Example2 - unpacking:
colors = ('black', 'blue', 'green', 'red') # packing
a, b, c, d = colors  # unpacking the given tuple
print(a)
print(b)
print(c)
print(d)


# Using " Asterisk* ":
# Asterisk is used when the number of variables is less than the number of values.
# You can add an '*' to the variable name and the values will be assigned to the variable as a list.

# Example:
fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
a, b, c, *d = fruits
print(a)
print(b)
print(c)
print(d)

# If the asterisk is assigned to another variable rather than the last variable, 
# then that variables collects all the values leaving the exact values left for the next variables.

# Example:
fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
a, *b, c, d = fruits
print(a)
print(b)
print(c)
print(d)



# Loop Tuples - Python:
# We can use both for and while loops for looping through a tuple.


# for loop:
# It is similar to the list loops.

# Example:
vehicles = ('car', 'bike', 'bicycle', 'train', 'flight')

for x in vehicles:
    print(x)

# We can also loop through the tuple by referring to their index number.
# Example:
vehicles = ('car', 'bike', 'bicycle', 'train', 'flight')

for x in vehicles:
    print(vehicles[0])


# Use range() and len() functions to a create a suitable iterable.
# Example:
vehicles = ('car', 'bike', 'bicycle', 'train', 'flight')

for x in range(len(vehicles)):
    print(vehicles[4])




# 'while' loop:
# We can loop through the tuple items by using the 'while' loop

# Example:
vehicles = ('car', 'bike', 'bicycle', 'train', 'flight')
i = 0
while i < len(vehicles):
   print(vehicles[i])
   i += 1



# Join tuples - Python:

# For joining two or more operators we use '+' operator.
# Example:
tuple1 = ('a', 'b', 'c', 'd')
tuple2 = ('e', 'f', 'g', 'h')

tuple3 = tuple1 + tuple2
print(tuple3)

# For multiplying the content of a tuple a given number of times, we can use the '*' operator.
# Example:
tuple1 = ('a', 'b', 'c', 'd')
tuple4 = tuple1*2  # given how many times the given values in the tuple should be multiplied.
print(tuple4)

 