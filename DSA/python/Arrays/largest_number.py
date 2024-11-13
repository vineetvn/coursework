
from typing import List


def largest(arr: List[int]) -> int:
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
        continue

    return largest


print(largest([25, 7, 5, 3, 64, 2, 53, 5, 46, 44]))
