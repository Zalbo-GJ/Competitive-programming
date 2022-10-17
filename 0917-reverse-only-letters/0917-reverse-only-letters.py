class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l = 0
        r = len(s)-1
        
        
        while l<r:
            if s[l].isalpha():
                if s[r].isalpha():
                    s[l],s[r] = s[r],s[l]
                    r-=1
                    l+=1
                else:
                    r-=1
            else:
                l+=1
        return "".join(s)