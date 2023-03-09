class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        
        for pos,spd in sorted(zip(position,speed))[::-1]:
            distance = (target - pos) / float(spd)
            
            if not stack or distance > stack[-1]:
                stack.append(distance)

        return len(stack)