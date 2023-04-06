class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        temp = []
        intLen = 1
        def backtrack(ind,dots):
            
            if dots == 4 and ind == len(s):
                ans.append(".".join(temp))
                return
            if dots > 4:
                return
            
            for i in range(ind, min(ind + 3, len(s))):
                if int(s[ind:i+1]) < 256 and (ind == i or s[ind] != "0"):
                    temp.append(s[ind:i+1])
                    backtrack(i+1, dots + 1)
                    temp.pop()
                        
        backtrack(0,0)
        
        return ans
                
            