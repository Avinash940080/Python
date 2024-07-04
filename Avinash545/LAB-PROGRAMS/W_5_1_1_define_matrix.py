r = int(input("Enter rows: "))
c = int(input("Enter columns: "))
A = []

for i in range(r):
    x = []
    for j in range(c):
        x.append(int(input()))
    A.append(x)

print("Matrix: ")
for i in range(r):
    for j in range(c):
        print(A[i][j], end=" ")
    print()
