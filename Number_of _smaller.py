n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
p1 = 0
p2 = 0
while p2 < m:
 
    if p1 >= n or arr1[p1] >= arr2[p2]:
 
        arr2[p2] = p1
        p2 += 1
    else:
 
        p1 += 1
 
print(*arr2)
