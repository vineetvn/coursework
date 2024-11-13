from typing import List


def isArraySorted(arr: List) -> bool:
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True


print(isArraySorted([1, 2, 3, 4, 10, 9]))
