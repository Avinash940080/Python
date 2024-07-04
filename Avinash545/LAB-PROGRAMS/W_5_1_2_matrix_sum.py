matOne = []
n = int(input("Enter n for matrix size of nxn matrix: "))
print("Enter elements of first matrix")

for i in range(n):
    x = []
    for j in range(n):
        x.append(int(input()))
    matOne.append(x)

print("Enter elements of second matrix")
matTwo = []
for i in range(n):
    x = []
    for j in range(n):
        x.append(int(input()))
    matTwo.append(x)

print("Sum of two matrices is:")
for i in range(n):
    for j in range(n):
        print(matOne[i][j] + matTwo[i][j], end=" ")
    print()
