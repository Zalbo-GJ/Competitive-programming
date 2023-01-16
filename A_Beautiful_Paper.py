n = int(input())

for _ in range(n):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    maxx = max(a1, a2, b1, b2)

    if a1+a2 == maxx and b1 == b2:
        print("Yes")
        continue
    elif a1+b2 == maxx and b1 == a2:

        print("Yes")
        continue
    elif b1+a2 == maxx and a1 == b2:
        print("Yes")
        continue
    elif b1+b2 == maxx and a1 == a2:
        print("Yes")
        continue
    else:
        print("No")
        continue
