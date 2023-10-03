class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def isSelfDividing(n):
            dig = list(map(int, str(n)))
            for num in dig:
                if num == 0 or n % num != 0:
                    return False
            return True
        
        ans = []
        for n in range(left, right + 1):
            if isSelfDividing(n):
                ans.append(n)
        
        return ans