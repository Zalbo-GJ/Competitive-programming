def selection(num):
    for i in range(len(num)):
        min = num[i]
        for j in range(i+1, len(num)):
            if num[j] < min:
                min = num[j]
        min, num[i] = num[i], min
    return num
