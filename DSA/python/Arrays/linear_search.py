def linear_search(arr: list, eleToSearch: int) -> int:
    for i in range(0, len(arr)):
        if arr[i] == eleToSearch:
            return i

    return -1


print(linear_search([0, 3, 6, 4, 2, 7], 4))  # 3

print(linear_search([0, 3, 6, 4, 2, 7], 4))  # -1
