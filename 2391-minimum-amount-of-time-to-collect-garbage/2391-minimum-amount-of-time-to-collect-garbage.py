class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        pre_sum = [0]
        curr = 0
        for idx in range(len(travel)):
            pre_sum.append(travel[idx] + curr)
            curr += travel[idx]
        ans = 0
        last_m, last_g, last_p = 0, 0, 0 
        for idx in range(len(garbage)):
            ans += len(garbage[idx])
            
            if "M" in garbage[idx]:
                last_m = idx
            if "G" in garbage[idx]:
                last_g = idx
            if "P" in garbage[idx]:
                last_p = idx

        ans += pre_sum[last_m] + pre_sum[last_g] + pre_sum[last_p]
        
        return ans
            
            