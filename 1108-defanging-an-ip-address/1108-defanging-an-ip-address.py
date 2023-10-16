class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        ans = []
        
        for val in address:
            if val == ".":
                ans.append("[.]")
                continue
            
            ans.append(val)
        
        return "".join(ans)