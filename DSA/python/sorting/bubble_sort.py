def bubble_sort(arr: list) -> list:
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort([9, 13, 12, 5, 4, 87, 43]))
