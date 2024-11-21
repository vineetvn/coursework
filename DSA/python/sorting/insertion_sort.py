def insertion_sort(arr: list) -> list:
    n = len(arr)

    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr


print(insertion_sort([9, 13, 12, 5, 4, 87, 43]))
