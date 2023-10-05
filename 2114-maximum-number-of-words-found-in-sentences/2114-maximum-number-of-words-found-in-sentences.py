class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        ans = 0
        
        for sen in sentences:
            sen = list(sen.split())
            ans = max(ans, len(sen))
        
        return ans