class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        arr = list(s1.split(" "))
        arr.extend(list(s2.split(" ")))
        
        count = Counter(arr)
        ans = []
        for word, count in count.items():
            if count == 1:
                ans.append(word)
        
        return ans