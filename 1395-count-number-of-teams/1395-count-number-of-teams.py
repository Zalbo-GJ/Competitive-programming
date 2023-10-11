class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        greater = [0] * len(rating)
        lower = [0] * len(rating)
        
        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    greater[i] += 1
                else:
                    lower[i] += 1
        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    ans += greater[j]
                else:
                    ans += lower[j]
        
        return ans
