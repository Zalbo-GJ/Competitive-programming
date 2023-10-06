class Solution:
    def minMaxGame(self, nums: List[int]) -> int:

        
        new_list = nums.copy()
        
        while True:
            
            if len(new_list) == 1:
                return new_list[0]
            
            temp = []
            even = False
            for idx in range(0, len(new_list) - 1, 2):
                if not even:
                    temp.append(min(new_list[idx], new_list[idx + 1]))
                else:
                    temp.append(max(new_list[idx], new_list[idx + 1]))
                    
                even = not even
            
            new_list = temp
        
        
            