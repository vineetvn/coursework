def selection_sort(arr: list) -> list:
    n = len(arr)

    if n < 2:
        return arr

    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(selection_sort([9, 13, 12, 5, 4, 87, 43]))
