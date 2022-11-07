class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        ascd, decd, ans, left = deque(), deque(), 0, 0
        for idx, n in enumerate(nums):
            while ascd and ascd[-1] > n: ascd.pop()
            while decd and decd[-1] < n: decd.pop()
            ascd.append(n)
            decd.append(n)
            if decd[0] - ascd[0] > limit:
                if decd[0] == nums[left]: decd.popleft()
                if ascd[0] == nums[left]: ascd.popleft()
                left += 1
            ans = max(ans, idx - left + 1)
        return ans