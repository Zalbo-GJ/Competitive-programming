# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))
    
    left = 0
    right = n - 1
    ans = "Yes"
    
    prev = float('inf')
    while left < right:
        
        
        pick = max(blocks[left],blocks[right])
        
        if pick > prev:
            ans = "No"
            
        if pick == blocks[left]:
            left += 1
        else:
            right -= 1
        
        prev = pick
       
            
    print(ans)
            
      
        
