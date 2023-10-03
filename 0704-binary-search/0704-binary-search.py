class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def recur(l, r):
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            if mid == l:
                if nums[r] == target:
                    return r
                return -1
            if nums[mid] < target:
                return recur(mid + 1, r)
            else:
                return recur(l, mid - 1)
        
        return recur(0 , len(nums) - 1)
            
            