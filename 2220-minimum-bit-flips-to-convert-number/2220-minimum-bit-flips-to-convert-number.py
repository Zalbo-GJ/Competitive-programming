class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin_start = bin(start)[:1: -1]
        bin_goal = bin(goal)[:1: -1]
        count_change = 0
        for idx in range(max(len(bin_start), len(bin_goal))):
            
            if idx >= len(bin_start):
                if idx < len(bin_goal) and bin_goal[idx] != "0":
                    count_change += 1
                
            elif idx >= len(bin_goal):
                if idx < len(bin_start) and bin_start[idx] != "0":
                    count_change += 1
                
            elif bin_start[idx] != bin_goal[idx]:
                count_change += 1
        
        return count_change
            
        
        