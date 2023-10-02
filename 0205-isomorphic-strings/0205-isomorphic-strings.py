class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dis = {}
        dit = {}
        for idx in range(len(s)):
            if s[idx] in dis and dis[s[idx]] != t[idx]:
                return False
            if t[idx] in dit and dit[t[idx]] != s[idx]:
                return False
     
            dis[s[idx]] = t[idx]
            dit[t[idx]] = s[idx]
            
        return True
                
            