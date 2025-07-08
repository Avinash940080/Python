# List items are indexed and you can access them by referring to the index number.
# index starts from '0'
# list_name[index no.]

# example
my_list=['apple','banana','mango','cherry']
print(my_list[0])

# Negative indexing is access the items form the last item
# It useful starts from index '-1' and continues

#example
my_list=['apple','banana','mango','cherry']
print(my_list[-1])


# Range of indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# syntax --> list_name[start:end]
# It doesnot include the last index the range.

#Example
my_list=['apple','banana','mango','cherry']
print(my_list[1:3])


# Range of negative indexes
# Use negative indexes if you want to start the search from the end of the list
# The syntax is similar to the normal index but reverse with negative sign.
# syntax --> list_name[-end: -start]
# same it doesnot include the starting index in the range

#Example
my_list=['apple','banana','mango','cherry']
print(my_list[-4:-1])


# We use 'in' to determine if a specific keyword is in the list or not.
# Example
my_list=['apple','banana','mango','cherry']
if 'guava' in my_list:
    print('yes, it is in the list')
else:
    print('not present')


# Change item value 
# To change the value of a specific item, refer to the index number.
# syntax --> list_name[index]=new value
# Example

my_list=['apple','banana','mango','cherry']
my_list[0] = 'guava'
print(my_list)

# Change the range of items
# To change the value of items within a specific range, define a list with the new values, 
# and refer to the range of index numbers where you want to insert the new values.
# syntax --> list_name[index range]=new values in the specific range.

# Example
my_list=['apple','banana','mango','cherry']
my_list[0:3] = ['guava','melon','kiwi']
print(my_list)


# Insert items 
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index.
# syntax --> list_name.insert('index no.','value')

# Example
my_list=['apple','banana','mango','cherry']
my_list.insert(0,'watermelon')
print(my_list)

# Add list items
# To add an item at the end of the list, use the append() method
# "syntax --> list_name.append('value')"

# Example
my_list=['apple','banana','mango','cherry']
my_list.append('melon')
print(my_list)

# Extend list
# To append elements from another list to the current list, use the extend() method.
# we can add any iterable elements to the currents list
# syntax --> 'current-list_name.append(another-list_name)'

# Example
my_list=['apple','banana','mango','cherry']
thislist=['melon','kiwi','guava','apple']

my_list.extend(thislist)
print(my_list)

# Remove list items
# remove() method removes the specifie item
# syntax --> "list_name.remove('value')"
# If there are more than  one occurence of an item then it will remove the first ocurred item.

#Example
my_list=['apple','banana','mango','cherry']
my_list.remove('apple')
print(my_list)

# Remove Specified Index
# The pop() method is used to remove the specified index.
# syntax --> "list_name.pop(index)"
# If you dont specify the index no. , it pops the last item 

# Example
my_list=['apple','banana','mango','cherry']
my_list.pop(0)
print(my_list)

# 'del' keyword also removes the specified index
# but it used on the very beginning of the syntax
# syntax --> "del list_name[index]"

# Example
my_list=['apple','banana','mango','cherry']
del my_list[0]
print(my_list)

# 'del' key can also be used to delete a complete list 
# syntax --> "del list_name"

# Example
my_list=['apple','banana','mango','cherry']
del my_list # deleted the entire list


# Clear the list
# The clear() method empties the list.
# The list still remains, but it has no content.
#  syntax --> "list_name.clear()"

# Example
my_list=['apple','banana','mango','cherry']
my_list.clear()
print(my_list)


# Loop lists

# For loops:
# Example:
my_list = ['apple', 'banana', 'cherry']

for x in my_list:
    print(x)

# Loop through the index numbers.
# You can also loog through the list items by referring to a their index number
# Use the range() and len() functions to create a suitable iterable.

# Example

my_list = ['apple', 'banana', 'cherry', 'guava']

for x in range(len(my_list)):
    print(my_list[x])


# while loops

# Example
my_list = ['apple', 'banana', 'cherry', 'guava']
x = 0
while x < len(my_list):
  print(my_list[x])
  x += 1

# List comprehensions
# List comprehensions offers a shorter syntax when you want to create a new list based on the values of an existing list.
# --------SYNTAX--------
# [expression "for" item "in" iterable "if" condition]

# Example1
my_list = [1, 2, 3, 4]

list = [x for x in my_list if x%2 == 0 ]
print(list)

# Example2
my_list = ['apple', 'banana', 'cherry', 'guava']

list = [ 'apple' for x in my_list]
print(list)



