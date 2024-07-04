n = int(input("Enter size of square matrix: "))
print("Enter elements of matrix A:")
A = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

B = []
print("Enter elements of matrix B:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    B.append(row)

C = []
for i in range(n):
    row = []
    for j in range(n):
        sum = 0
        for k in range(n):
            sum += A[i][k] * B[k][j]
        row.append(sum)
    C.append(row)

print("Matrix multiplication result is:")
for i in range(n):
    for j in range(n):
        print(C[i][j], end=" ")
    print()
