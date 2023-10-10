class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        words = title.split(" ")
        ans = []
        for word in words:
            if len(word) > 2:
                ans.append(word[0].capitalize() + word[1:].lower())
            else:
                ans.append(word.lower())
        
        return " ".join(ans)
            