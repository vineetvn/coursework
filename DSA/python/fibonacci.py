def fibonacci_number(n):
    fibA, fibB = 0, 1

    for i in range(2, n+1):
        fibA, fibB = fibB, fibA + fibB
    return fibB
