class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        
        new_list = nums.copy()
        while True:
            
            if len(new_list) == 1:
                return new_list[0]

            temp = []
            for idx in range(len(new_list) - 1):
                temp.append((new_list[idx] + new_list[idx + 1]) % 10)
            
            new_list = temp
        
        
            