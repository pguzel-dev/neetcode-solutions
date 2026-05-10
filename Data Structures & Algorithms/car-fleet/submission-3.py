# Derived solution
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        stack.append((target - cars[0][0]) / cars[0][1])

        for (pst, spd) in cars[1:]:
            time = ((target - pst) / spd)
            if time > stack[-1]:
                stack.append(time)
        
        return len(stack)


            

