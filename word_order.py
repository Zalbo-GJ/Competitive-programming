# Enter your code here. Read input from STDIN. Print output to STDOUT

integer = int(input())
counter = {}

for _ in range(integer):
    
    strin = input()
    
    if strin in counter:
        
        counter[strin] += 1 
    else:
        counter[strin] = 1
    
print(len(counter))
for i in counter:
    print(str(counter[i]), end=" ")
