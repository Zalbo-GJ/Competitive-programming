def domino(m, n):
    a = (m*n)/2
    print(int(a))


ipt = input(
    "enter two digit numbers that is the size of the domino board with *x* in the middle example-2x5-")
m = ipt.split('x')


domino(int(m[0]), int(m[1]))
