class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        def maxSum(L , M):
            maxL = ans = 0
            for i in range(L + M,len(pSum)):
                maxL = max(maxL,pSum[i-M] - pSum[i-M-L])
                ans = max(ans,maxL+pSum[i]-pSum[i-M])
            return ans

        pSum = [0] * (len(nums)+1)
        for i, a in enumerate(nums):
            pSum[i + 1] = pSum[i] + a
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))