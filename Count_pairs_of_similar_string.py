class Solution:
    def similarPairs(self, words: List[str]) -> int:

        ans = 0
        
        for i in range(len(words)-1):
            hash1 = Counter(words[i])

            for j in range(i+1,len(words)):
                hash2 = Counter(words[j])

                if hash1.keys() == hash2.keys():
                    ans+=1
        return ans
