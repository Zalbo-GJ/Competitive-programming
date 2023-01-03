from collections import Counter
t = int(input())
for _ in range(t):

    ans = 0
    n, cost = input().split(" ")
    planets = list(map(int, input().split(" ")))
    count = Counter(planets)

    for key in count:

        if int(cost) < count[key]:
            ans += int(cost)
        else:
            ans += count[key]
    print(ans)
