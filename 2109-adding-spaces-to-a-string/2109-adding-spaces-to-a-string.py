class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        ans = []
        p = 0
        for i in range(len(s)):
            
            if p < len(spaces) and i == spaces[p]:
                ans += " "
                p+=1
            ans.append(s[i])
            
        return "".join(ans)
        