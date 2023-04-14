t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    
    mat = []
    for _ in range(m):

        row = list(map(int, input().split()))

        mat.append(row)

    right_diagonal = {}
    left_diagonal = {}

    for j in range(n):
        i = 0
        summ = 0
        while i < m and j < n:
            summ += mat[i][j]
            if i+j not in left_diagonal:
                left_diagonal[i+j] = mat[i][j]
            else:
                left_diagonal[i+j] += mat[i][j]
            i += 1
            j += 1
        right_diagonal[i-j] = summ
            
    for i in range(1,len(mat)):
        j = 0
        summ = 0
        while i < m and j < n:
            summ += mat[i][j]
            if i+j not in left_diagonal:
                left_diagonal[i+j] = mat[i][j]
            else:
                left_diagonal[i+j] += mat[i][j]
            i += 1
            j += 1
        right_diagonal[i-j] = summ
            


    ans = 0
    
    for row in range(m):
        for col in range(n):
            summ = left_diagonal[row + col] + right_diagonal[row - col] - mat[row][col]
            ans = max(ans, summ)
    
    print(ans)
