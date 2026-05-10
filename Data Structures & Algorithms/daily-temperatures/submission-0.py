class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                results[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            stack.append((index, temp))
        
        return results

