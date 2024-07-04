def generate_all_binary_strings(n, arr, i):
    if i == n:
        print(*arr)
        return
    arr[i] = 0
    generate_all_binary_strings(n, arr, i + 1)
    arr[i] = 1
    generate_all_binary_strings(n, arr, i + 1)


# Example usage:
n = 0
arr = [0] * n
generate_all_binary_strings(n, arr, 0)