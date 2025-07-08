

# Python - sort list

# Sort list alphanumerically
# List objects have a 'sort()' method that will sort the list alphanumerically, ascending, by default:
# ---------SYNTAX-----------
# listname.sort()

# Example(sort the list alphabetically):
my_list = ['orange', 'kiwi', 'mango', 'pineapple', 'banana']
my_list.sort()  #sorts the elements in the list alphabetically
print(my_list)


# Example(sort the list numerically)
my_list = [100, 50, 65, 82, 23]
my_list.sort()
print(my_list)


# Sort descending
# To sort descending, use the keyword argument
# reverse = True:

# Example(reverse alphabetical order)
my_list = ['orange', 'kiwi', 'mango', 'pineapple', 'banana']
my_list.sort(reverse=True)
print(my_list)

# Example(descending order)
my_list = [100, 50, 65, 82, 23]
my_list.sort(reverse=True)
print(my_list)


# Case Insensitive sort
# By default the sort() is case sensitve, resulting in all capital letters being sorted before lower case letters.

# Example
my_list = ['Orange', 'Kiwi', 'mango', 'pineapple', 'banana']
my_list.sort()
print(my_list)

# We can use built in functions as key functions when sorting a list.
# If you want a case-sensitive sort function, use str.lower as a key function.

# Example
my_list = ['orange', 'kiwi', 'mango', 'Pineapple', 'Banana']
my_list.sort(key=str.lower)
print(my_list)

# Reverse order
# The reverse() method reverses the current order of the given list.

# Example
my_list = ['orange', 'kiwi', 'mango', 'pineapple', 'banana']
my_list.reverse()
print(my_list)



# Python - Copy List

# Use the built-in method copy() to copy a list.
# Another way to copy a list is by using the list() method.
# Slice operator ':' can also be used to copy a list.

# Example - using copy() method.
my_list = ['orange', 'kiwi', 'mango', 'pineapple', 'banana']
new_list = my_list.copy()
print(new_list)


# Example - using list() method.
my_list = ['orange', 'kiwi', 'mango', 'pineapple', 'banana']
new_list = list(my_list)
print(new_list)

# Example - using slice ':' operator.
my_list = ['orange', 'kiwi', 'mango', 'pineapple']
new_list = my_list[:]
print(new_list)



# Python - Join Lists.

# We can join or concatenate, two or more list using several ways. They are:
# 1. Using the '+' between two lists
# 2. Using append() method appending all the items in one list to another list one by one.
# 3. Using extend() method for adding the list2 at the end of list1


# Example-1
list1 = ['apple', 'banana', 'orange']
list2 = ['pineapple', 'kiwi', 'mango']

list3 = list1 + list2
print(list3)


# Example-2
list1 = ['apple', 'banana', 'orange']
list2 = ['pineapple', 'kiwi', 'mango']

for x in list2:
    list1.append(x)

print(list1)


# Example-3
list1 = ['apple', 'banana', 'orange']
list2 = ['pineapple', 'kiwi', 'mango']

list1.extend(list2)
print(list1)