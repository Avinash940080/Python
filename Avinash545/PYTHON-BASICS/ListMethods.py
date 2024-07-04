# Creating a sample list
my_list = [1, 2, 3, 4, 5]

# append() - Adds an element at the end of the list
my_list.append(6)
print("append():", my_list)

# extend() - Extends the list by appending elements from the iterable
my_list.extend([7, 8, 9])
print("extend():", my_list)

# insert() - Inserts an element at the specified position
my_list.insert(0, 0)
print("insert():", my_list)

# remove() - Removes the first occurrence of the specified value
my_list.remove(3)
print("remove():", my_list)

# pop() - Removes the element at the specified position (or the last element if no position is specified) and returns it
popped_element = my_list.pop(4)
print("pop():", my_list, "Popped element:", popped_element)

# index() - Returns the index of the first occurrence of the specified value
index = my_list.index(5)
print("index():", index)

# count() - Returns the number of occurrences of the specified value
count = my_list.count(2)
print("count():", count)

# reverse() - Reverses the elements of the list in place
my_list.reverse()
print("reverse():", my_list)

# sort() - Sorts the elements of the list in place
my_list.sort()
print("sort():", my_list)

minimum = min(my_list)
print("min():", minimum)

# max() - Returns the largest element in the list
maximum = max(my_list)
print("max():", maximum)

# del - Deletes the element at the specified index
del my_list[2]
print("del:", my_list)

# copy() - Returns a shallow copy of the list
copied_list = my_list.copy()
print("copy():", copied_list)

# index() - Returns the index of the first occurrence of the specified value
index = my_list.index(5)
print("index():", index)


# clear() - Removes all elements from the list
my_list.clear()
print("clear():", my_list)
