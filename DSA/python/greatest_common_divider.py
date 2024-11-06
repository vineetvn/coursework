def gcdComputer(a, b):
    if b == 0:
        return a
    else:
        return gcdComputer(b, a%b)

# This is called the euclidean algorithm