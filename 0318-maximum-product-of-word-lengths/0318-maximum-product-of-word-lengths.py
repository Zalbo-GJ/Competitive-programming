class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = defaultdict(int)
        
        for word in words:
            bit = 0
            for char in word:
                bit |= (1<< (ord(char)-97))
            dic[word] = bit
        maxx = 0
        for i in words:
            for j in words:
                
                if not (dic[i] & dic[j]):
                    maxx = max(maxx, len(i) * len(j))
                    
        
        return maxx
                    