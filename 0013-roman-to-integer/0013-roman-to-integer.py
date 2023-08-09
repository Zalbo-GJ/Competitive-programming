class Solution:
    def romanToInt(self, s: str) -> int:
        
        i = 0
        summ = 0 
        while i < len(s):
            match (s[i]):
                case "M":
                    summ += 1000
                    i += 1
                    continue
                case "D":
                    summ += 500
                    i += 1
                    continue
                case "C":
                    if i + 1 < len(s) and s[i + 1] == "M":
                        summ += 900
                        i += 2
                        continue
                    elif i + 1 < len(s) and s[i + 1] == "D":
                        summ += 400
                        i += 2
                        continue
                    else:
                        summ += 100
                        i += 1
                        continue
                case "L":
                    summ += 50
                    i += 1
                    continue
                case "X":
                    if i + 1 < len(s) and s[i + 1] == "C":
                        summ += 90
                        i += 2
                        continue
                    elif i + 1 < len(s) and s[i + 1] == "L":
                        summ += 40
                        i += 2
                        continue
                    else:
                        summ += 10  
                        i += 1
                        continue
                case "V":
                    summ += 5 
                    i += 1
                    continue
                case "I":
                    if i + 1 < len(s) and s[i + 1] == "X":
                        summ += 9
                        i += 2
                        continue
                    elif i + 1 < len(s) and s[i + 1] == "V":
                        summ += 4
                        i += 2
                        continue
                    else:
                        summ += 1
                        i += 1
                        continue
           
        return summ
                    