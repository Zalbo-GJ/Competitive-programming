class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s= s[::-1]
        i = 0
        while i < len(s):
            if(s[i]!="["):
                stack.append(s[i])
                i+=1
            elif(s[i]=="["):
                m = ""
                while stack[-1]!="]":
                    m+=stack.pop()
                stack.pop()
                i+=1
                num = ""
                while(i<len(s) and s[i].isdigit() ):
                    num = s[i] + num
                    i+=1
                stack.append(m*int(num))
        return "".join(stack[::-1])