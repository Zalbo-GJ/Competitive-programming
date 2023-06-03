class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstInt = float("inf")
        secondInt = float("inf")
        
        for num in nums:
            if num < firstInt:
                firstInt = num
            elif firstInt < num < secondInt:
                secondInt = num
            elif firstInt < secondInt < num:
                return True
          
        return False