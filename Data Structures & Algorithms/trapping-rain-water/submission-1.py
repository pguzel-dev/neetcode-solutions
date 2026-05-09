class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        max_before = [0] * n
        max_after = [0] * n

        for i in range(1, n):
            max_before[i] = max(max_before[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            max_after[i] = max(max_after[i + 1], height[i + 1])

        result = 0

        for i in range(n):
            water_level = min(max_before[i], max_after[i])
            if water_level > height[i]:
                result += water_level - height[i]

        return result