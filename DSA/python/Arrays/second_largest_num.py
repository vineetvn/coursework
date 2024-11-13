def second_largest(arr: list) -> int:
    largest = arr[0]
    sLargest = arr[1]

    for num in arr:
        if num > largest:
            sLargest = largest
            largest = num
        elif num < largest and num > sLargest:
            sLargest = num

    return sLargest


print(second_largest([25, 7, 5, 3, 64, 2, 53, 5, 46, 64]))
