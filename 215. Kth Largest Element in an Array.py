class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k
        def recur(l,r):
            piv = nums[r]
            ptr = l
            
            for ind in range(l,r):
                if nums[ind] <= piv:
                    nums[ind], nums[ptr] = nums[ptr], nums[ind]
                    ptr += 1
            
            nums[ptr], nums[r] = nums[r], nums[ptr]

            if ptr < k:
                return recur(ptr+1,r)
            elif ptr > k:
                return recur(l, ptr-1)
            else:
                return nums[ptr]
        
        return recur(0, len(nums)-1)
        
       
                    
        
