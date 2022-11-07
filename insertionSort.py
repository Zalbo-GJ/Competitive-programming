def insertion(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i-1
        while j > 0 and key < num[j]:
            num[j+1] = num[j]
            j -= 1
        num[j+1] = key
    return num
