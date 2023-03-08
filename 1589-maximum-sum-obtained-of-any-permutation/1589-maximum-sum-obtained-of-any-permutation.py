class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        arr = [0 for _ in range(len(nums)+ 5)]
        
        for start, end in requests:
            
            arr[start] += 1
            arr[end+1] -= 1

        
        for ind in range(1, len(arr)):
            arr[ind] +=  arr[ind - 1]
        
        arr.sort(reverse = True)
        nums.sort(reverse = True)
        
        
        ans  = 0
        
        for ind in range(len(nums)):
            ans += arr[ind] * nums[ind]
        
        return ans % ((10**9) + 7)
            
            
        
        