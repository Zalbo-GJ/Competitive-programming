class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        cnt = Counter(letters)
        tmp = []
        def backtrack(count, idx):
            nonlocal score, words, tmp
            
            if idx == len(words):
                return 0
            
            jump = backtrack(count, idx + 1)
            sc = 0
            c = count.copy()
            breaked = False
            for char in words[idx]:
                if not c[char]:
                    sc = 0
                    breaked = True
                    break
                    
                sc += score[ord(char) - ord('a')]
                c[char] -= 1
            if breaked:
                c = count
            take =  sc + backtrack(c, idx + 1)
             
            return max(jump, take)
        
        return backtrack(cnt, 0)