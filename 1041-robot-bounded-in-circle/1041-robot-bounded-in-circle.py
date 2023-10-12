class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        visited = set((0,0))

        curr = [0, 0, "N"]
        for char in instructions:
            if char == "G":
                if curr[2] == "N":
                    curr[1] += 1
                elif curr[2] == "E":
                    curr[0] += 1
                elif curr[2] == "W":
                    curr[0] -= 1
                elif curr[2] == "S":
                    curr[1] -= 1
            elif char == "L":
                if curr[2] == "N":
                    curr[2] = "W"
                elif curr[2] == "E":
                    curr[2] = "N"
                elif curr[2] == "W":
                    curr[2] = "S"
                elif curr[2] == "S":
                    curr[2] = "E"
            elif char == "R":
                if curr[2] == "N":
                    curr[2] = "E"
                elif curr[2] == "E":
                    curr[2] = "S"
                elif curr[2] == "W":
                    curr[2] = "N"
                elif curr[2] == "S":
                    curr[2] = "W"
        if (curr[0], curr[1]) == (0, 0):
            return True
        if curr[2] != "N":
            return True
        
            
        return False
                