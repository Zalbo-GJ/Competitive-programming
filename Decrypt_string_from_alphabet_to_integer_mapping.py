class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        d = {}
        for i,letter in enumerate(alphabets):
            d[str(i+1)] = letter
        
        res = ""
        dig =""
        i = len(s)-1
        while i >= 0:
            if s[i] != "#":
                res += d[s[i]]
            else:
                dig = s[i-2] + s[i-1]
                res += d[dig]
                i-=2
            i-=1
        return res[::-1]
