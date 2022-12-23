class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0
        res = ""

        while i<len(word1) and i < len(word2):
            
            res += word1[i] + word2[i]
            i+=1
        while i < len(word1):
            res += word1[i]
            i+=1
        while i < len(word2):
            res += word2[i]
            i+=1
            
        return res
