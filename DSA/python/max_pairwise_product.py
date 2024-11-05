def max_pairwise_product(numbers: list[int]):
    n = len(numbers)
    max_num1 = 0
    max_num1_index = 0
    max_num2 = 0
    for i in range(n):
        if numbers[i] > max_num1:
            max_num1 = numbers[i]
            max_num1_index = i

    for j in range(n):
        if j == max_num1_index:
            continue
        if numbers[j] > max_num2:
            max_num2 = numbers[j]
    return max_num1 * max_num2


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
