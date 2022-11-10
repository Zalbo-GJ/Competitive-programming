class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        ans = []
        
        nums.sort()
        
        for i in range(len(queries)):
            mx = 0
            presum =  0
            for j in range(len(nums)):
                presum += nums[j]
                
                if presum <= queries[i]:
                    mx = max(mx, j+1)
                else:
                    break
                
                
            ans.append(mx)
            
        return ans