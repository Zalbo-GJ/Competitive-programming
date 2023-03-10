class Solution:
    def decodeString(self, s: str) -> str:
        
        ans = ""
        
        if s.isdigit():
            return ans
        def split(string):
            res = []
            temp = []
            brace_count = 0
            nested = 0
            for i in string:
                if i.isdigit():
                    
                    if temp and brace_count == 0 and not temp[-1].isdigit():
                        res.append("".join(temp))
                        temp = []
                    temp.append(i)
                elif i == "[":
                    brace_count += 1
                    nested += 1
                    temp.append(i)
                elif i == "]":
                    brace_count -= 1
                    temp.append(i)
                    if brace_count == 0:
                        res.append("".join(temp))
                        temp = []
                else:
                    temp.append(i)
            
            if temp:
                 res.append("".join(temp))
                    
                    
            return [nested, res]
        
            
        def recur(string):
            
            
            nested, st = split(string)
            
            if nested == 0:
                return st[0]
            
            dummy = []
            for i in st:
                if i[0].isdigit():
                    p = 0
                    while i[p].isdigit(): p += 1
                    num = int(i[0:p])
                    i = recur("".join(i[p+1:-1])) * num
                    
                dummy.append(i)
            
            return "".join(dummy)
                    
            
        ans = recur(s)
        
        return ans        
                
                  
        
        
        
        
        