def binary_search(arr, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if arr[middle] == target:
        return middle

    elif arr[middle] > target:
        return binary_search(arr, target, left, middle - 1)

    else:
        return binary_search(arr, target, middle + 1, right)


a = [-2, 0, 2, 6, 7, 9]
if __name__ == '__main__':
    print(binary_search(a, 9, 0, len(a)-1))
