# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))
n = int(input())
ans = True
for _ in range(n):
    sett = set(map(int, input().split()))
    
    if not A.issuperset(sett):
        ans = False 
        break
print(ans)
        
        
