class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        root = {}
        
        L = len(bin(max(nums))) - 2
        nums = [[(num >> i) & 1 for i in range(L)[::-1]] for num in nums]
        ans = 0
        ''
        for num in nums:
            curr = root
            xor_node = root
            curr_xor = 0
            for bit in num:
                
                if bit not in curr:
                    curr[bit] = {}
                curr = curr[bit]
                
                toggled_bit = 1 - bit
                
                if toggled_bit in xor_node:
                    xor_node = xor_node[toggled_bit]
                    curr_xor = (curr_xor << 1) |  1
                else:
                    xor_node = xor_node[bit]
                    curr_xor = (curr_xor << 1)
            ans = max(ans, curr_xor)
                    
        return ans
        