class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        
        for emp in hours:
            if emp >= target:
                ans += 1
        
        return ans