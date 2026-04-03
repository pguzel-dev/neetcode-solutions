# Brute force
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        for left in range(len(heights)):
            for right in range(left+1, len(heights)):
                breadth = (right - left)
                depth = min(heights[right], heights[left])
                water = breadth * depth
                max_water = max(max_water, water)
        return max_water

        