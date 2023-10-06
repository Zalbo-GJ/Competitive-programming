class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            new_list = [s[i:i+k] for i in range(0, len(s), k)]
            s = ''
            for dig in new_list:
                s += str(sum([int(n) for n in dig]))
        return s