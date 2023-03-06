class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        presum = [0 ] * len(s)

        for start, end, direction in shifts:
     
            if direction == 1:
                presum[start] += 1
                if end + 1 < len(presum):
                    presum[end + 1] -= 1
            else:
                presum[start] -= 1
                if end + 1 < len(presum):
                    presum[end + 1] += 1
        
        
        for ind in range(1,len(presum)):
            
            presum[ind] += presum[ind-1]
      
        ans = []
        
        for ind in range(len(s)):
            char = (ord(s[ind]) + presum[ind]) - 97
            char %= 26
            char += 97

            ans.append(chr(char))

        return "".join(ans)
        
        
        
        
                
            