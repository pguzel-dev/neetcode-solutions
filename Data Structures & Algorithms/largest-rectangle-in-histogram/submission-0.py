class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        result = 0

        left_smaller = [-1] * n
        right_smaller = [n] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_smaller[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_smaller[i] = stack[-1]
            stack.append(i)
        
        for i in range(n):
            area = heights[i] * (right_smaller[i] - left_smaller[i] - 1)
            result = max(result, area)
        
        return result
