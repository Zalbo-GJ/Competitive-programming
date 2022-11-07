import math


def theatre(m, n, a):
    length = math.ceil(m/a)
    width = math.ceil(n/a)
    print(length * width)


theatre(17, 8, 4)
