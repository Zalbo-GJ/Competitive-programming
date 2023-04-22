from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

def bicolor(node, c):
    if not color[node]:
        color[node] = c
    else:
        return color[node] == c
    
    for nd in lookup[node]:

        if not bicolor(nd, 2 if c == 1 else 1):
            return False
        
    return True

i = True
while i:
    n = int(input())
    if not n:
        break

    e = int(input())
    color = [0 for _ in range(n+5)]
    lookup = defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())

        lookup[a].append(b)
        lookup[b].append(a)
    flag = True
    for nd in range(1, n+1):
        if not color[nd] and not bicolor(nd, 1):
            if flag:
                print("NOT BICOLOURABLE.")
            flag = False
            break

    if flag:
        print("BICOLOURABLE.")
