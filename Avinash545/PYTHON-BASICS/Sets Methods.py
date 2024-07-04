# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Adding elements to a set
set1.add(6)
print("Set after adding element:", set1)

# Removing elements from a set
set1.remove(3)
print("Set after removing element:", set1)

# Union of sets
union_set = set1.union(set2)
print("Union of sets:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# Difference of sets
difference_set = set1.difference(set2)
print("Difference of sets (set1 - set2):", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of sets:", symmetric_difference_set)

# Checking if a set is a subset or superset of another set
print("Is set1 a subset of set2?", set1.issubset(set2))
print("Is set1 a superset of set2?", set1.issuperset(set2))

# Checking for disjoint sets
print("Are set1 and set2 disjoint?", set1.isdisjoint(set2))

# Removing all elements from a set
set1.clear()
print("Set after clearing:", set1)

# Creating sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Copying a set
set3 = set1.copy()
print("Copied set:", set3)

# Checking the length of a set
print("Length of set1:", len(set1))

# Checking if an element is in a set
print("Is 2 present in set1?", 2 in set1)

# Checking if an element is not in a set
print("Is 5 not present in set1?", 5 not in set1)

# Removing an element from a set using discard()
set1.discard(3)
print("Set1 after discarding 3:", set1)

# Removing an arbitrary element from a set using pop()
popped_element = set2.pop()
print("Popped element from set2:", popped_element)
print("Set2 after popping element:", set2)

# Clearing a set
set3.clear()
print("Cleared set3:", set3)
