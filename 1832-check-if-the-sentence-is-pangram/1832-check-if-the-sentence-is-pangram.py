class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        existence = set(sentence)
        
        return len(existence) == 26