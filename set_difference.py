n = int(input())
set1 = set(map(int, input().split()))
m = int(input())
set2 = set(map(int, input().split()))

print(len(set1.difference(set2)))
