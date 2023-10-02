class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.ans = float('inf')
        self.stones = stones
        self.dp(0, 0, 0)
        
        return self.ans
    @cache
    def dp(self,left_cup, right_cup, idx):
            
            if idx >= len(self.stones):
                self.ans = min(self.ans, abs(left_cup - right_cup))
                return
            
            self.dp(left_cup + self.stones[idx], right_cup, idx + 1)
            self.dp(left_cup, right_cup + self.stones[idx], idx + 1)
        