class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # max_before[i] stores the tallest bar to the left of index i
        max_before = [0] * n
        # max_after[i] stores the tallest bar to the right of index i
        max_after = [0] * n

        # Fill max_before from left to right
        for i in range(1, n):
            max_before[i] = max(max_before[i - 1], height[i - 1])

        # Fill max_after from right to left
        for i in range(n - 2, -1, -1):
            max_after[i] = max(max_after[i + 1], height[i + 1])

        total_water = 0

        # Calculate trapped water at each index
        for i in range(n):
            # Water level depends on the shorter surrounding wall
            water_level = min(max_before[i], max_after[i])

            # Only add water if the current bar is below the water level
            if water_level > height[i]:
                total_water += water_level - height[i]

        return total_water