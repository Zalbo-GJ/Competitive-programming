n = int(input())

arr = list(map(int, input().split(" ")))

l = 0
r = n-1
flag = True
if l == r:
    print(1, 0)
    flag = False
    pass
sumL = arr[l]
sumR = arr[r]

while l < r-1:

    if sumL < sumR and l < r-1:
        l += 1
        sumL += arr[l]
    if sumL > sumR and l < r-1:
        r -= 1
        sumR += arr[r]
    if sumL == sumR and l < r-1:
        if l+1 == r-1:
            l += 1
        else:
            l += 1
            r -= 1
            sumL += arr[l]
            sumR += arr[r]
if flag:
    print(l+1, n-r)
