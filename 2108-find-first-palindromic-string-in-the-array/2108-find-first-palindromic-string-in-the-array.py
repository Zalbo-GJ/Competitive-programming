class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        
        for i in words:
            start = 0
            end = len(i)-1
            
            while start < end:
                if i[start] != i[end]:
                    break
                
                start+=1
                end-=1

            if start >=end:
                return i
        return ""
        
                
            
            