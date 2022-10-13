class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        stack = []
        
        for pos, spd in sorted(zip(position,speed))[::-1]:
            t = (target-pos)/ float(spd)    # the time it takes to get to target
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)