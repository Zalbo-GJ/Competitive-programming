class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k>0:
            final=code+code[:k]
            for i in range(len(code)):
                code[i]=sum(final[i+1:k+1+i])
            return code
        if k==0:
            new=[0]*len(code)
            return new
        else:
            final=code[k:]+code
            for i in range(len(code)):
                code[i]=sum(final[i:i-k])
            return code