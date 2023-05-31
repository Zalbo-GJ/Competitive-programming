class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        state = [float('inf') for _ in range(amount + 1)]
        state[0] = 0
        
        for idx in range(1, amount + 1):
            for coin in coins:
                if idx - coin >= 0:
                    state[idx] = min(state[idx], state[idx - coin])
            
            state[idx] += 1
                    
        return state[-1] if state[-1] != float('inf') else -1
        
        
        
        
        
        

        