class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        comment_count = 0

        string = ""
        for line in source:
            i = 0
            while i < len(line):
                if comment_count > 0:
                    if line[i] == '*' and i+1 < len(line) and line[i+1] == '/':
                        comment_count -= 1
                        i+=1
                else:
                    if line[i] == '/' and i+1 < len(line) and line[i+1] == '*':
                        comment_count += 1
                        i+=1
                    elif line[i] == '/' and i+1 < len(line) and line[i+1] == '/' :
                        break 
                    if comment_count==0:
                        string += line[i]   
                i+=1 
            if string and comment_count==0:
                res.append(string)  
            if comment_count==0:
                string = ""
        return res                      
