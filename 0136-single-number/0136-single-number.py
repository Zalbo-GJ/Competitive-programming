class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        l = [[i,j] for i,j in count.items()]
        l.sort(key= lambda x : x[1])
        
        return l[0][0]