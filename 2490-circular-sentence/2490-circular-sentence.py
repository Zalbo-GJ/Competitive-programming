class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        
        if words[-1][-1] != words[0][0]:
            return False
        for idx in range(1, len(words)):
            if words[idx - 1][-1] != words[idx][0]:
                return False
        
        return True