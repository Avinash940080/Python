# You are using Python
rows = int(input())
cols = int(input())

matrix = []

for i in range(rows):
    elements = list(map(int, input().split(' ')))
    matrix.append(elements)

print(f'Original Array: ')
for row in matrix:
    print("[", " ".join(map(str, rows)), "]")
    print(row)

tras = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        tras[j][i] = matrix[i][j]

print(f'Transposed Array: ')
for row in tras:
    print(row)
    


        
    
    
    




