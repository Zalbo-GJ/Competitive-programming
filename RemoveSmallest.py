t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = list(map(int, input().split()))

    arr.sort()

    l = 0
    r = 1
    while r < len(arr):

        if  arr[r] - arr[l] < 2:
            del(arr[l])
        else:
            l += 1
            r += 1
    
    if len(arr) == 1:
        print("YES")
    else:
        print("NO")
