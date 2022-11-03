class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        l = r = 0
        word = list(word)
        
        while r<len(word):
            
         
            if word[r] == ch:
                while l < r:
                    word[l],word[r] = word[r],word[l]
                    r-=1
                    l+=1
                return "".join(word)
            r+=1
        return "".join(word)