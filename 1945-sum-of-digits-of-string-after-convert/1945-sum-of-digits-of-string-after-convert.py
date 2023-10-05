class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        num = []
        for char in s:
            num.append(str(ord(char) - ord('a') + 1))
        num = "".join(num)
        
        while k > 0:
            digs = list(map(int, str(num)))
            num = 0
            for i in digs:
                num += i
            k -= 1         
        
        return num