class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        ans = []
        l = 0 
        h = len(s)
        
        for i in s:
            if i == "I":
                ans.append(l)
                l+=1
            else:
                ans.append(h)
                h-=1
        ans.append(l)
        return ans