class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        
        smaller = []
        greater = []
        count = 0
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                count += 1
                
        return smaller + [pivot for i in range(count)] + greater
        
        