class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        ans = 0
        
        for idx in range(len(startTime)):
            if endTime[idx] >= queryTime and startTime[idx] <= queryTime:
                ans += 1
        
        return ans
                