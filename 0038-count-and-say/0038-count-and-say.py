class Solution:
    def countAndSay(self, n: int) -> str:
        say = ['1']
        temp = []
        for _ in range(n-1):
            
            l = 0
            r = 0
            while r < len(say):
                
                if r + 1 == len(say) or say[r + 1] != say[l]:
                    temp.append(str(r - l + 1))
                    temp.append(str(say[l]))
                    l = r + 1
    
                r += 1
            say = temp
            temp = []
        
        return "".join(say)