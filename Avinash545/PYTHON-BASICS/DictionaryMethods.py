# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Accessing items
print("Items in the dictionary:", my_dict.items())

# Accessing keys
print("Keys in the dictionary:", my_dict.keys())

# Accessing values
print("Values in the dictionary:", my_dict.values())

# Accessing a value using a key
print("Value associated with key 'a':", my_dict.get('a'))

# Adding a new item
my_dict['e'] = 5
print("Updated dictionary after adding new item:", my_dict)

# Removing an item using key
removed_item = my_dict.pop('c')
print("Removed item:", removed_item)
print("Updated dictionary after removing item:", my_dict)

# Removing the last item
last_item = my_dict.popitem()
print("Removed last item:", last_item)
print("Updated dictionary after removing last item:", my_dict)

# Copying a dictionary
new_dict = my_dict.copy()
print("Copied dictionary:", new_dict)

# Checking if a key exists
print("Is 'b' present in the dictionary?", 'b' in my_dict)

# Length of the dictionary
print("Length of the dictionary:", len(my_dict))

# Merging dictionaries
other_dict = {'e': 5, 'f': 6}
my_dict.update(other_dict)
print("Merged dictionary:", my_dict)

# Removing a specific key-value pair
del my_dict['d']
print("Updated dictionary after deleting key 'd':", my_dict)

# Removing and returning an arbitrary item (Python 3.7+)
arbitrary_item = my_dict.popitem()
print("Removed arbitrary item:", arbitrary_item)
print("Updated dictionary after removing arbitrary item:", my_dict)

# Accessing a value using a key and providing a default value if key doesn't exist
value = my_dict.setdefault('z', 26)
print("Value associated with key 'z' (default value if not exists):", value)
print("Updated dictionary after setting default value:", my_dict)

# Creating a new dictionary with keys from sequence and values set to a default value
keys = ['x', 'y', 'z']
default_value = 0

new_dict = dict.fromkeys(keys, default_value)
print("New dictionary created from keys with default value:", new_dict)

# Clearing the dictionary
my_dict.clear()
print("Cleared dictionary:", my_dict)


