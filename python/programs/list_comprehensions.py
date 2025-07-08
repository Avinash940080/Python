# List comprehensions:
# A list comprehension is a concise way to create lists in Python.
# It provides a shorter and more readable way to generate lists compared to using loops.
# Syntax --> new_list = [expression for item in iterable if condition].

# Example:
# Creating a list.
squares = [x**2 for x in range(1, 6)]
print(squares)

# Using an 'if' condition:
evens = [x for x in range(10) if x%2 == 0]
print(evens)

# Nested list comprehensions:
nested = [[1,2,3],[4,5,6],[7,8,9]]

item_list = [item for sublist in nested for item in sublist]
print(item_list)


# nested list comprehensions:
# We can create and manipulate nested lists using list comprehensions.
# We can only use this 

# Example:
result = [[i**2 for i in range(1,6)] for j in range(1,4)]
print(result)


# Using input function for taking input from the user:
# Example:

main = []

n = 0
while True:
    n += 1
    print(f'enter the first elements of sublist {n} separated by comma:')
    sub = [[int(a) for a in input().split(',')]]
    main.extend(sub)
    stop = input('If the sublists are completed enter ''stop''')
    if stop.lower() == 'stop':
        break

print(main)


