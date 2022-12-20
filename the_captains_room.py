# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
k = int(input())
rooms = list(map(int, input().split()))

count = defaultdict(int)

for room in rooms:
    count[room] +=1
    
for room in count:
    if count[room] != k:
        print(room)
        break
