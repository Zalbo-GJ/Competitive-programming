def bubble(num):
    for _ in range(len(num)):
        for i in range(1, len(num)):
            if num[i] < num[i-1]:
                num[i], num[i-1] = num[i-1], num[i]
    return num
