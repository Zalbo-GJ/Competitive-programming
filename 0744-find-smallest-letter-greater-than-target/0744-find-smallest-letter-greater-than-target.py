class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        ans = 0
        
        for idx in range(len(letters)):
            if letters[idx] > target:
                if ans and letters[idx] < ans:
                    ans = letters[idx]
                if not ans:
                    ans = letters[idx]
        
        return ans if ans else letters[0]
                    