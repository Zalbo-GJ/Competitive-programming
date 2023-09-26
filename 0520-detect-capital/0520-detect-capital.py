class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        isAllCap = False
        if word[-1].isupper():
            isAllCap = True
        for idx in range(len(word)-1 , -1 , -1):
            if isAllCap:
                if word[idx].islower():
                    return False
            
            else:
                if not word[idx].islower() and idx > 0:
                    return False
        
        return True
            
            