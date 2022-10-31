class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = 0
        s = list(s)
        while start < len(s):
            
            if start+1 == len(s) or s[start+1] == " ":
                j = start
                while j > end:
                    s[end],s[j] = s[j],s[end]
                    end+=1
                    j-=1
                start +=2
                end = start
            else:      
                start +=1
        return "".join(s)
                