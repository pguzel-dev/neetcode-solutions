# Suggested Solution
class Solution:  
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = zip(position, speed)
        stack = []

        for pos, spd in sorted(pairs, reverse=True):
            time_to_target = (target - pos) / spd
            stack.append(time_to_target)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)