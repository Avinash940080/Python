arr1 = []
arr2 = []

print("Enter array elements of 1st array : ")
for i in range(0, 6):
    element = int(input("Enter element {}: ".format(i + 1)))
    arr1.append(element)

print("Enter array elements of 2nd array : ")  # Corrected typo
for i in range(0, 6):
    element = int(input("Enter element {}: ".format(i+1)))
    arr2.append(element)

common_array = []

print("Common elements in arrays are : ")
for i in arr1:
    if i in arr2:
        common_array.append(i)

print(common_array)
