class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            if row[0] < 0:
                ans += len(row)
                continue
            l = 0
            r = len(row) - 1
            n = len(row)
            while l <= r:
                mid = (l + r) // 2
                if row[mid] >= 0:
                    l = mid + 1
                elif row[mid] < 0 and row[mid - 1] >= 0:
                    ans += n - mid 
                    break
                elif row[mid] < 0:
                    r = mid - 1
                
        return ans
            