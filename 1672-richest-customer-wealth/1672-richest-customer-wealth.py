class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        accounts.sort(key = lambda x: sum(x))
    
        return sum(accounts[-1])