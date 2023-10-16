class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        pre = [0]
        
        for idx in range(1,len(nums)):
            pre.append(nums[idx - 1] + pre[-1])
        post = [0]
        for idx in range(len(nums) -2, -1, -1):
            post.append(nums[idx +  1] + post[-1])
        
        post = post[:: -1]
        
        for idx in range(len(nums)):
            pre[idx] = abs(pre[idx] - post[idx])
        
        return pre
        
        