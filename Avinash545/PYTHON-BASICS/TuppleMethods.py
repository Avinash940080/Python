# Creating a sample tuple
my_tuple = (1, 2, 3, 4, 5, 3, 6)

# count() - Returns the number of times the specified value appears in the tuple
count = my_tuple.count(3)
print("count():", count)

# index() - Returns the index of the first occurrence of the specified value in the tuple
index = my_tuple.index(4)
print("index():", index)

# len() - Returns the number of items in the tuple
length = len(my_tuple)
print("Length of the tuple:", length)

# tuple() - Converts an iterable to a tuple
my_list = [6, 7, 8, 9, 10]
converted_tuple = tuple(my_list)
print("Converted tuple:", converted_tuple)