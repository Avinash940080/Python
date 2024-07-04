def remove(li):
    unique =[]
    for i in li:
        if i not in unique:
            unique.append(i)
    return unique

li=[1,2,3,3,4,5,5]
print("Original = ",li)
print("removed list = ",remove(li))
