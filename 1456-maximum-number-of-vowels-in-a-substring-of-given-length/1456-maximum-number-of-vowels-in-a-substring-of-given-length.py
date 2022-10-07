class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count =ans=0
        for i in range(len(s)):
            
            if s[i] in "aeiou":
                count+=1
            if i > k-1:  #no need to slide until the window size is full
                if s[i-k] in "aeiou":
                    count -=1

            ans = max(ans,count)
        return ans