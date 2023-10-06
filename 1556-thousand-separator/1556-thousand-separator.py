class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = []
        count = 0
        for dig in str(n)[::-1]:
            if count == 3:
                ans.append(".")
                count = 0
            ans.append(dig)
            count += 1
            
        
        return "".join(ans[::-1])