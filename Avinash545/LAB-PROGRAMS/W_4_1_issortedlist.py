def is_sorted(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i-1]<=arr[i]:
            continue
        else:
            return False
    return True


arr =[1,2,3,4,5,8,1]
print(is_sorted(arr))