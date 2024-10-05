import random


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
        if numbers[j] > max_num2:
            max_num2 = numbers[j]
    return max_num1 * max_num2

n = random.randint(1,5)
print(n)
numbers = random.sample(range(1,10), n)
print(numbers)
print(max_pairwise_product(numbers))



# if __name__ == '__main__':
#     _ = int(input())
#     input_numbers = list(map(int, input().split()))
#     print(max_pairwise_product(input_numbers))
