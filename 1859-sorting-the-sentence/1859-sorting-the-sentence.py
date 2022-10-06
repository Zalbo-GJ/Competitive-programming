class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = s.split(" ")
        ans = [0]*len(s)
        
        for i in range(len(s)):
            sentence = ""
            for l in s[i]:
                
                if (l.isdigit()):
                
                    ans[int(l)-1] = str(sentence)
                    
                else:
                    sentence += l
                
                
        return " ".join(ans)