class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        power_fact = pow(power, k-1, modulo)
        
        k_hash = 0 
        match_idx = -1 
        
        for i, char in enumerate(reversed(s)): 
            if i >= k: 
                k_hash -= (ord(s[len(s) - i + k - 1]) - ord('a') + 1) * power_fact
            k_hash = (k_hash * power + (ord(char) - ord('a') + 1)) % modulo
            
            if i >= k-1 and k_hash == hashValue: 
                match_idx = len(s) - i - 1
        
        if match_idx != -1:
            return s[match_idx: match_idx + k]
        return ""