# Remove set items - Python:

# To remove an item in a set, use the remove(), or the discard() method.
# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will not raise an error.

# Example:
set1 = {'apple', 'banana', 'orange', 'kiwi', 'mango'}
print(set1)
set1.remove('apple')
print(set1)
set1.discard('banana')
print(set1)


# pop() method is used remove a random item from the given set.
# It is not which item is getting removed.
# return value of the pop() method is the removed item.

# Example:
set1 = {'apple', 'banana', 'orange', 'kiwi', 'mango'}
item = set1.pop()
print(item)
print(set1)


# The clear() method is used to empty the given set.
# Example:
set1 = {'apple', 'banana', 'orange', 'kiwi', 'mango'}
set1.clear()
print(set1)

# The 'del' keyword is used to delete a set permanently.
# Example:
set1 = {'apple', 'banana', 'orange', 'kiwi', 'mango'}
del set1



# Loop Sets - Python:

# We can use through the set items by using a 'for' loop.
# Example:
set1 = {'apple', 'banana', 'orange', 'kiwi', 'mango'}
for i in set1:
    print(i)




# Join Sets - Python:

"""
 There are several ways to join two or more sets in python.

 1.The union() and update() methods joins all items from both sets.
 2.The intersection() method keeps only the duplicates.
 3.The difference() method keeps the items from the first set that are not in other set(s).
 4.The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

# 1.union() method returns a new set with all items from both sets.
#   Using union() method, we can also join more than 2 sets.
#   We can use '|' operator instead of the 'union()' method, and you will get the same result.


# Example:
set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 8, 9, 10}

set3 = set1.union(set2)
print(set3)


# Example:
set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 8, 9, 10}

set3 = set1 | set2
print(set3)


# Join a set and a tuple:

# Example:
x = {1, 2, 3, 4, 5, 6}
y = (7, 8, 9, 10)

z = x.union(y)
print(z)


# update() method inserts all items from one set into another.
# The update() method changes the original set, and does not return a new set.
# Note - Both union() and update() will exclude any duplicate items.

# Example:
set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 8, 9, 10}

set1.update(set2)
print(set1)




# Intersection:
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# it returns the common items in given both sets.
# intersection() can be used to join between a set and another datatype.
# We can use the '&' operator instead of 'intersection()' method, and you will get the same result

# Example-1:
set1 = {1, 2, 3, 4, 5, 6, 8, 10}
set2 = {7, 8, 9, 10, 4, 5, 3}

set3 = set1.intersection(set2)
print(set3)

# Example-2:
# '&' doesnot allow us to join sets with other datatypes
set1 = {1, 2, 3, 4, 5, 6, 8, 10}
set2 = {7, 8, 9, 10, 4, 5, 3}

set3 = set1 & set2
print(set3)


# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# Example:
set1 = {1, 2, 3, 4, 5, 6, 8, 10}
set2 = {7, 8, 9, 10, 4, 5, 3}

set1.intersection_update(set2)
print(set1)


# The values 'True' and '1' are considered the same value. The same goes for 'False' and '0'.
# Example:
set1 = {1, 2, 3, 4, 5, 6, 8, 10, False}
set2 = {7, 8, 9, 10, 4, 5, 3, True, 0}

set3 = set1.intersection(set2)
print(set3)


# Difference:

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# Basically, it returns  all unique items from the given 2 sets into a new set.
# '-' operator can be used instead of difference().
# '-' doesnot allow us to join sets with other datatypes, unlike difference().

# Example-1:
set1 = {1, 2, 3, 4, 5, 6, 8, 10}
set2 = {7, 8, 9, 10, 4, 5, 3}

set3 = set1.difference(set2)
print(set3)

# Example-2:
set1 = {1, 2, 3, 4, 5, 6, 8, 10}
set2 = {7, 8, 9, 10, 4, 5, 3}

set3 = set1 - set2
print(set3)


# difference_update():
# It is the same thing but it doesnot return in a new set, instead it will update it the given set.

# Example:
set1 = {1, 2, 3, 4, 5, 6, 8, 10}
set2 = {7, 8, 9, 10, 4, 5, 3}

set1.difference_update(set2)
print(set1)


# Symmetric Differences:
# The symmetic_difference() method will keep only the elements that are NOT present in both sets.
# We can use the '^' operator instead of the symmetric_difference() method, and you will get the same result.
# The '^' operator doesnot allow us to join a set with another datatype, unlike symmetric_difference() method.

# Example-1:
set1 = {1, 2, 3, 4, 5, 6, 8, 10}
set2 = {7, 8, 9, 10, 4, 5, 3}

set3 = set1.symmetric_difference(set2)
print(set3)


# Example-2:
set1 = {1, 2, 3, 4, 5, 6, 8, 10}
set2 = {7, 8, 9, 10, 4, 5, 3}

set3 = set1 ^ set2
print(set3)


# symmetric_difference_update():
# It is the same thing but it doesnot return in a new set, instead it will update it the given set.

# Example:
set1 = {1, 2, 3, 4, 5, 6, 8, 10}
set2 = {7, 8, 9, 10, 4, 5, 3}

set1.symmetric_difference_update(set2)
print(set1)