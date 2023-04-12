n = int(input())
k = int(input())
mat = [[]for _ in range(k)]
for _ in range(k):
    inpt = list(map(int, input().split()))
    if inpt[0] == 1:
        mat[inpt[1]-1].append(inpt[2])
        mat[inpt[2]-1].append(inpt[1])

    else:
        print(*mat[inpt[1]-1])



