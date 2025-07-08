# Dictionaries:
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and donot allow duplicates.
# Dictionaries are written in curly brackets and have keys and values.


# example
this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}

print(this_dict1)

# The dictionary items can be referred by using the key name.
# Example:

this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}

print(this_dict1['model'])


# To determine how many items a dictionary has, we use the len() function:
# Example:

this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}

print(len(this_dict1))


# The values in dictionary items can be of any datatype:
# Example - string, int , boolean, and list datatypes:

this_dict1 = {
    'brand':'ford',
    'electric':False,
    'year':1964,
    'colors':['black','blue','green']

}

print(this_dict1)

print(type(this_dict1))


# The dict() constructor:
# It is also possible to use the dict() constructor to make a dictionary.

# Example:

this_dict1 = dict(name = 'jarvis', age = 17, country = 'USA')
print(this_dict1)



# Python - Accessing dictionary items:
# Accessing items:
# You can access the items of a dictionary by referring to its key name, inside square brackets
# Example:

this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}

x = this_dict1['model']
print(x)

# We can also use the get() method for getting the same result.
this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}

x = this_dict1.get('brand')
print(x)


# Get keys.
# The keys() method will return a list of all the keys in the dictionary.

# Example:

this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}

x = this_dict1.keys()
print(x)

# Any changes done to the dictionary will be reflected in the keys list.
# Example:

this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}
x = this_dict1.keys()
print(x)

this_dict1['color'] = 'black'
print(x)


# Get values:
# values() method will return a list of all the values in the dictionary.

# Example:
this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}

x = this_dict1.values()
print(x)

# Any changes done to the dictionary will be reflected in the values list.
# Example:

this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}
x = this_dict1.values()
print(x)

this_dict1['color'] = 'black'
print(x)


# Get items:
# The items() method will return each item in a dictionary, as tuples in a list.

# Example:
this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}
x = this_dict1.items()
print(x)


# Any changes done to the dictionary will be reflected in the items list.
# Example:

this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}
x = this_dict1.items()
print(x)

this_dict1['year'] = 2020
print(x)

# We can add new item to the original dictionary, and see that the items in the list gets updated as well:

# Example:
this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}
x = this_dict1.items()
print(x)

this_dict1['color'] = 'black'
print(x)



# Check if Key Exists;
# To determine if a spcified key is present in a dictionary use the 'in' keyword:

# Example:
this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}

if 'model' in this_dict1:
    print('yes')
else:
    print('no')



# Python - Change Dictionary Items:

# Change values:
# You can change the value of a specific item by reffering to its key name:

# Example:
this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}

this_dict1['year'] = 2025
print(this_dict1)


# Update Dictionary:
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

# Example:

this_dict1 = {
    'brand':'ford',
    'model':'mustang',
    'year':'1964'
}

this_dict1.update({'year':2022})
print(this_dict1)