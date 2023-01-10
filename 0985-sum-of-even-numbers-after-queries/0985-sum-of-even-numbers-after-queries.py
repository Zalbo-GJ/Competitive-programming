class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_sum = 0
        ans = []
        for i in nums:
            if i % 2 == 0:
                even_sum += i
        
        for val, index in queries:
            
            if nums[index] % 2 == 0:
                if (nums[index] + val ) % 2 == 0:
                    even_sum += (nums[index] + val) - nums[index]
                    
                else:
                    even_sum -= nums[index]
            else:
                if (nums[index] + val ) % 2 == 0:
                    even_sum += (nums[index] + val)
            nums[index] += val
            ans.append(even_sum)
        
        return ans
                
        