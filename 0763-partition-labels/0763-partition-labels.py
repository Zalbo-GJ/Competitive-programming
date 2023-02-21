class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
            
            
            
        ans = []  
        maxInd = 0
        j = 0
        for i in range(len(s)):
            maxInd = max(maxInd, d[s[i]])
            
            if i == maxInd:
                ans.append(maxInd+1-j)
                j = maxInd+1
                
        return ans