class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d = Counter(s[:len(p)-1])
        pDict = Counter(p)
        
        start = 0
        ans = []
        
        for i in range(len(p)-1,len(s)):
            d[s[i]] +=1
            if d==pDict:
                ans.append(start)
            d[s[start]] -= 1
            if d[s[start]] == 0:
                del d[s[start]]
            start +=1
        return ans
                