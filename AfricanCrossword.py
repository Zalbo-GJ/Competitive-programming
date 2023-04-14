from collections import Counter


n, m = map(int, input().split())

mat = []
colwise = [[] for _ in range(m)]
for _ in range(n):
    st = input()
    row = []
    for ind in range(m):
        row.append(st[ind])
        colwise[ind].append(st[ind])
    mat.append(row)
colCount = []
for i in range(m):
    count = Counter(colwise[i])
    colCount.append(count)

ans = []
for row in range(n):
    rowCount = Counter(mat[row])
    for col in range(m):
        

        if rowCount[mat[row][col]] == 1 and colCount[col][mat[row][col]] == 1:
            ans.append(mat[row][col])

print("".join(ans))

