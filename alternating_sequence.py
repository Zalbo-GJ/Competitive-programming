t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    maxSum = 0
    curr = arr[0]

    for ind in range(1, n):

        if arr[ind] * arr[ind-1] > 0:
            curr = max(curr, arr[ind])
        else:
            maxSum += curr
            curr = arr[ind]
    
    maxSum += curr

    print(maxSum)

            
