class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rCount = Counter(ransomNote)
        mCount = Counter(magazine)
        
        for char in ransomNote:
            if rCount[char] > mCount[char]:
                return False
        
        return True