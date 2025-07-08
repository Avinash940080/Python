# Python - sets:
# sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable, and unindexed.
# Set  items are unchangeable, but you can remove items and add new items.
# sets are written in curly brackets.
# sets don't return dupllicate values.

# Example:
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Sets are unordered, so yo cannot be sure in which order the items will appear.
# Sets doesnot allow duplicate items.

# Example:
# In sets, 'true' and '1' are considered as same values. So it prints the value which is assigned first.
# Same applies for 'false' and '0'
my_set = {1, 2, 3, 4, 5, True, 5, 6} 
print(my_set)



# Length of a set:
# len() built in method is used to determine the length of a set. 

# Example:
my_set = {1, 2, 3, 4, 5}
print(len(my_set))


# A set an be of any datatype.
# Example:
set1 = {1, 2, 3, 4, 5}
print(set1)
set2 = {True, False, False}
print(set2)
set3 = {'apple', 'banana', 'orange'}
print(set3)

# set() constructor is used to make set.
my_tuple = (1, 2, 3, 4, 5)
set = set(my_tuple)
print(set)


# Accessing set items:
# Unlike lists or tuples, we cannot access items in a st by reffering to an index or a key.
# But we can loop through the set items using a 'for' loop, or ask if specified value is present in a set, by using the 'in' keyword.

# Example:
set3 = {'apple', 'banana', 'orange'}

for x in set3:
    print(x)
    print('banana' in set3) # checking if the item is present in the set.

# Example:
set3 = {'apple', 'banana', 'orange'}
print('banana' not in set3) # checking if the items is not present in the set.

# Once a set is created, you cannot change its items, but you can add new items.

# Add Set items:
# To add one item to a set use the 'add()' method.

# Example:
set3 = {'apple', 'banana', 'orange'}
set3.add('kiwi')
print(set3)


# Add sets:
# To add items from another set into the current set, use the update() method.

# Example:
current_set = {'apple', 'banana', 'orange'}
new_set = {'kiwi', 'pineapple', 'mango'}

current_set.update(new_set)   # moved all the items in the new state to the current set.
print(current_set)

# update() method doesnot have to be a set, it can be any iterable object(lists, tuples)

# Example:
set = {'apple', 'banana', 'orange'}
list = ['pineapple', 'mango', 'kiwi']

set.update(list)
print(set)