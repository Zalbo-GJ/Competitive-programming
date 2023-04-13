n = int(input())

mat = [[]for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            mat[i].append(j+1)


ans = 0
visited = set()
for ind in range(n):
    for i in range(len(mat[ind])):
        if tuple([mat[ind][i], ind+1]) not in visited and tuple( [ ind+1, mat[ind][i]]) not in visited and mat[ind][i] != ind+1:
            ans += 1 
        visited.add(tuple( [mat[ind][i], ind+1]))
        visited.add(tuple( [ ind+1, mat[ind][i]]))

print(ans )
