# Python - Add Dictionary Items.

# Adding items:
# Adding an item to the dictionary is done by using a new index key and assingning a value to it.

# Example:
thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

thisdict['color'] = 'black'
print(thisdict)



# Update Dictionary:
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.


# Example:

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

thisdict.update({'color':'red'})
print(thisdict)



# Python - Remove Dictionary Items.
# Removing Items.
# There are several methods to remove items from a dictionay:



# pop():
# pop() method removes the item with the specified key name:

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

thisdict.pop('model')
print(thisdict)


# popitem() method removes the last inserted item.
# Example:

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

thisdict.popitem()
print(thisdict)



# the 'del' keyword removes the item with the specified key name:
# Example:
thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

del thisdict['brand']
print(thisdict)


# del keyword can also be used to delete the dictionary entirely.
# Example:

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

del thisdict # The given dictionary is deleted permanently.


# clear() method empties the dictionary:
# Example:

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

thisdict.clear()
print(thisdict)



# Python - Loop Dictionaries.


# Loop Through a Dictionary
# We can loop through a dictionary by using a 'for' loop.
# When looping through a dictionary, the return value are the 'keys' of the dictionary.

# Example:
thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}
for items in thisdict:
    print(items)

# This will print the values of the dictionary.
for items in thisdict:
    print(thisdict[items])


# We can also loop through the vaues in a dictionary using the values() method.
# Example

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

for items in thisdict.values():
    print(items)


# Similarily we can use keys() method for returning the key values.
# Example:

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

for items in thisdict.keys():
    print(items)



# items()
# We can loop through both keys and values, by using the items() methos:

thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

for x, y in thisdict.items():
    print(x, y)



# Python - Copy Dictionaries.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
# Example:
thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

thisdict1 = thisdict.copy()
print(thisdict1)

# Another way to make a copy is to use the built-in function dict().
# Example:
thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964
}

thisdict2 = dict(thisdict)
print(thisdict2)



# Nested dictionaries - Python:
# It is considered as dictionary in a dictionary.

# Example:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)


# We can also add  all the dictionaries to the main dictionary.
# Example:
child1 = {
    "name" : "Emil",
    "year" : 2004
  }
child2 = {
    "name" : "Tobias",
    "year" : 2007
  }
child3 = {
    "name" : "Linus",
    "year" : 2011
  }


family = {
    'child1':child1,
    'child2':child2,
    'child3':child3
}

print(family)


# We can access the nested dictionaries by reffering to the keys of the dictionaries.
# Example:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

x = myfamily['child1']['name'] #access the name in the child dictionary from my family dictionary.
print(x)


# We can also update the values of the nested dictionary.
# Example:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

myfamily['child1']['year'] = 2003
print(myfamily['child1']['year'])

# looping through nested dictionary.
# We can achieve it by using 'items()' method.

# Example:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : '2004'
  },
  "child2" : {
    "name" : "Tobias",
    "year" : '2007'
  },
  "child3" : {
    "name" : "Linus",
    "year" : '2011'
  }
}

for x, obj in family.items():
    print(x)
    for y in obj:
        print(y + ':',obj[y])
