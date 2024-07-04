# comment line

''' Multiple line comments using '
    1.String copy
    2.String compare
    3.String concat
    4.Slicing
'''

# string can be declared between ' '
str1 = "cmr"
str2 = 'engineering college'
print(str1)
print(str2)

#copying
str3=str2
print(str3)

#concatating
#str4 = str1+str2
str4 = str1+" "+ str2
print(str4)

#check equal or not
x = (str3==str4)
print(x)

#slicing
str='cmr engineering college'
k = str[0:3]
print(k)
str7='cmr engineering college'
p = str7[0:-2]
print(p)

# Defining a string
my_string = "Hello, World!"

# Length of the string
print("Length of the string:", len(my_string))

# Accessing individual characters
print("First character of the string:", my_string[0])
print("Last character of the string:", my_string[-1])

# Slicing the string
print("Substring from index 7 to end:", my_string[7:])
print("Substring from index 7 to 12:", my_string[7:12])

# Concatenating strings
new_string = my_string + " Welcome!"
print("Concatenated string:", new_string)

# Repeating a string
repeated_string = my_string * 3
print("Repeated string:", repeated_string)

# Converting to lowercase and uppercase
print("Lowercase:", my_string.lower())
print("Uppercase:", my_string.upper())

# Capitalizing the first character of the string
print("Capitalized string:", my_string.capitalize())

# Counting occurrences of a substring
print("Number of occurrences of 'l':", my_string.count('l'))

# Finding the index of a substring
print("Index of 'World':", my_string.find('World'))

# Checking if the string starts or ends with a specific substring
print("Starts with 'Hello':", my_string.startswith('Hello'))
print("Ends with 'World':", my_string.endswith('World'))

# Replacing a substring with another substring
new_string = my_string.replace('World', 'Universe')
print("String after replacement:", new_string)

# Splitting the string into a list of substrings
split_string = my_string.split(',')
print("Split string:", split_string)

# Joining a list of substrings into a single string
joined_string = ','.join(split_string)
print("Joined string:", joined_string)

# Stripping leading and trailing whitespace
my_string_with_spaces = "   Hello, World!   "
print("Stripped string:", my_string_with_spaces.strip())
