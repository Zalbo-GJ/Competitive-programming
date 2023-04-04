class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        def Gcd(a, b):
            if b == 0:
                return a
            
            return Gcd(b, a%b)
        
        return Gcd(nums[0], nums[-1])
        