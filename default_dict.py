# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
A=[]
for _ in range(n):
    A.append(input())
for j in range(m):
    bol = False
    B = input()
    for i in range(n):
        if B == A[i]:
            print(i+1,end=" ")
            bol = True
    if not bol :
        print("-1", end = " ")
        bol = False
        
    print()



    
