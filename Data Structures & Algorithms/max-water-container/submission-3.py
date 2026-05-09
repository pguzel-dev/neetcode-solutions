class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            # water = breadth * depth
            water_amount = (right - left) * min(heights[right], heights[left])
            max_water = max(water_amount, max_water)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water