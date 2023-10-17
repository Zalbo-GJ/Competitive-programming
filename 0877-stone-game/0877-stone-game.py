class Solution:
    def stoneGame(self, piles):
        N = len(piles)

        @lru_cache(None)
        def dp(i, j, my_turn):
            if i > j: return 0
            if my_turn:
                return max(piles[i] + dp(i+1,j,not my_turn), piles[j] + dp(i,j-1,not my_turn))
            else:
                return min(-piles[i] + dp(i+1,j,not my_turn), -piles[j] + dp(i,j-1,not my_turn))

        return dp(0, N - 1, True) > 0