class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        stack = []
        
        for i in nums2:
            while stack and stack[-1] < i :
                d[stack.pop()] = i
            stack.append(i)
            
        for i in range(len(nums1)):
            if nums1[i] in d:
                nums1[i]= d[nums1[i]]
            else:
                nums1[i] = -1
        return nums1