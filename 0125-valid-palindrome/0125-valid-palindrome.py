class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        
        while l<r:
            while l<r and not s[l].isalnum():l+=1
            while l<r and not s[r].isalnum():r-=1
           
            if s[l].lower() != s[r].lower():
                return False
            r-=1
            l+=1
        return True