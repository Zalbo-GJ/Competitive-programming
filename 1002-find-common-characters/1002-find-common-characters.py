class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        """
        1. count the first element and set as bestcase answr
        2. check each count of element from 1 to n if element of ans exist and take the min count
        """
        
        best = Counter(words[0])
      
        ans = []
        for i in range(1, len(words)):
            ele = Counter(words[i])
            
            for char in best:
                if ele[char] > 0:
                    best[char] = min(best[char], ele[char])
                else:
                    best[char] = 0
                    
        for i in best:
            for _ in range(best[i]):
                ans.append(i)
            
        return ans