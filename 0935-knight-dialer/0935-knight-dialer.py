class Solution:
    def knightDialer(self, n: int) -> int:
        
        moves = [[4, 6], [8, 6], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        ans = 0
        m = 10 ** 9 + 7
        @cache
        def dp(curr, p_number):
            if p_number == n:
                return 1
            ans = 0
            for land in moves[curr]:
                ans = (ans + dp(land, p_number + 1)) % m
            
            return ans
        
        for i in range(10):
            ans = (ans + dp(i, 1)) % m
        
        return ans % m