class Solution:
    def interpret(self, command: str) -> str:

        res = ""
        for i in range(len(command)):
            if command[i] == "G":
                res += "G"
            elif command[i] == "(":
                if command[i+1] == "a":
                    res += "al"
                    i+=3
                elif command[i+1] == ")":
                    res += "o"
                    i+=2
        return res
