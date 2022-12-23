class Solution:
    def compare(self, word1, word2, d):
        if len(word1) < len(word2):
            print("inside")
            for j in range( len(word1) ):
                if d[word1[j]] > d[word2[j]]:
                    return False
                elif d[word1[j]] < d[word2[j]]:
                    return True

            return True
        else:
            for j in range( len(word2) ):
                if d[word1[j]] > d[word2[j]]:
                    return False
                elif d[word1[j]] < d[word2[j]]:
                    return True
            return len(word1) == len(word2)
        # hello   hel
       # hello leetcode 
            


    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i ,l in enumerate(order):
            d[l] = i

        
        res = True
        for i in range(len(words)-1):
            res = res and self.compare(words[i],words[i+1],d)   
        
        return res



        
        
