t = int(input())

for _ in range(t):

    n = int(input())
    arr = list(map(int, input().split()))
    flag = False
    summ = zero_count = 0
    for i in range(n-1):

        if arr[i] != 0:
            flag = True
            summ += arr[i]
        else:
            if flag:
                zero_count += 1

    print(summ + zero_count)
