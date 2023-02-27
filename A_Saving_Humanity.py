t = int(input())

for _ in range(t):

    n, m = map(int, input().split())

    arr = list(map(int, input()))
    ans = [i for i in arr]
    for _ in range(m+1):

        arr = [i for i in ans]
        for i in range(len(arr)):

            if arr[i] == 0:

                if i-1 < 0:
                    if arr[i+1] == 1:
                        ans[i] = 1
                elif i+1 == n:
                    if arr[i-1] == 1:
                        ans[i] = 1

                else:
                    if arr[i+1] + arr[i-1] == 1:
                        ans[i] = 1
        if arr == ans:
            break
    print("".join(list(map(str, arr))))
