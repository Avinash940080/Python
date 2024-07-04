def has_duplicate(arr):
    n = len(arr)
    uniq = []
    for i in range(0,n):
        if arr[i] in arr:
            return True
        else:
            continue
    return False


arr =[1,2,3,4,5,6]
print(has_duplicate(arr))