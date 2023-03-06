class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def winner( l, r, turn):
            
            if l == r:
                return turn * nums[l]
            
            
            left = turn * nums[l] + winner(l + 1, r, -turn)
            right = turn * nums[r] + winner(l, r - 1, -turn )
        
        
        
            return turn * max(turn * left, turn * right)
        
        
        return winner(0,len(nums)-1, 1) >=0