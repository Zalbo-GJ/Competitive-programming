n = int(input())

for _ in range(n):
    input()
    chess = []
    for i in range(8):
        row = list((input()))
        chess.append(row)

    for i in range(1, 7):

        for j in range(1, 7):

            if chess[i][j] == "#":
                if chess[i-1][j+1] == "#" and chess[i-1][j-1] == "#":
                    print(i+1, j+1)
                    break
