# Matrix:

# Matrices are fundamental structures in mathematics and computer science, 
# representing rectangular arrays of numbers arranged in rows and columns.
# In python, matrices can be implemented using basic data structures or specialized libraries.


# Creating a matrix:

# Matrix Intialization:
# A matrix can be intialized using nested lists.

# Example:
matrix = [ [1,2,3],
           [4,5,6], 
           [7,8,9] ]


# Accessing a elements in a matrix:
# We can access elements in a matrix using index elements of rows and cols.
# Syntax ---> matrix[rows][cols]

# Example:
matrix = [ [1,2,3],
           [4,5,6], 
           [7,8,9] ]

element = matrix[2][2]
print(element)


# Iterating through a matrix:
# Use nested loops to iterate through each element in the sublist.

# Example:
matrix = [ [1,2,3],
           [4,5,6], 
           [7,8,9] ]

for i in matrix:
    for j in i:
        print(j, end=' ')

        
# Matrix manipulation:
# We can modify a matrix by accessing them through their indices.

# Example:
matrix = [ [1,2,3],
           [4,5,6], 
           [7,8,9] ]

matrix[0][2] = 10
print(matrix)


# Matrix Operations:
# We can perform basic operations like addition, subtraction and multiplication using nested loops.

# Example:
matrix1 = [ [1,2,3],
           [4,5,6], 
           [7,8,9] ]

matrix2 = [[9,8,7],
           [6,5,4],
           [3,2,1]]


result = []

for i in range(len(matrix1)):  # looping through no.of rows
    row = []
    for j in range(len(matrix1[0])): # looping through no.of columns
        row.append(0)
    result.append(row)
print(result)

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
print(result)


# Example - Using nested list comprehensions:
matrix1 = [ [1,2,3],
            [4,5,6], 
            [7,8,9] ]

matrix2 = [[9,8,7],
           [6,5,4],
           [3,2,1]]


result = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
print(result)



# Creating a matrix by taking input from the user:
'''

--> Define the dimensions(rows, columns) of the matrix by taking the input from the user
--> Intialize an empty matrix
--> Collect the row data and append it to the empty matrix if no.of rows are equal to no.of columns.
--> Display the matrix

'''

# Example:
rows = int(input('enter the no.of rows: '))
cols = int(input('enter the no.of columns: '))

result = []
for i in range(rows):
        print(f'Enter the elements in the row {i}: ')
        a = list(map(int, input().split(',')))
        if rows == cols:
            result.append(a)
        else:
            print('Error: enter the no.of rows correctly')
            break
print(f'The resultant matrix is:{result}')

for row in result:
    print(row)

        

