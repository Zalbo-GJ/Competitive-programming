class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1_count = Counter(words1)
        w2_count = Counter(words2)
        ans = 0
        for word, count in w1_count.items():
            if count == 1 and w2_count[word] == 1:
                ans += 1 
        
        return ans
                