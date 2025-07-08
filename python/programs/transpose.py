# Transpose of a matrix:
# We can transpose a given matrix by intializing a resultant matrix by '0's and 
# interchange the rows and columns of the two matrices.


# Example:
rows = int(input())
cols = int(input())

matrix = []

for i in range(rows):
        elements = list(map(int, input().split(' ')))
        matrix.append(elements)

print(f'The Original {rows}*{cols} matrix is: ')
for row in matrix:
     print(row)

res = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        res[j][i] = matrix[i][j]

print(f'The transposed of {rows}*{cols} matrix is: ')
for row in res:
     print(row)