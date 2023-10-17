class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        nums = list(str(n))
        
        multiple = 1
        summ = 0
        
        for num in nums:
            multiple *= int(num)
            summ += int(num)
        
        return multiple - summ