n = int(input())
matrix = []
for r in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


ans = [[] for _ in range(n)]

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 1:
            ans[row].append(col+1)

for lst in ans:
    print(len(lst), *lst)
