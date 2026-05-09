class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        max_before = [0] * n
        max_after = [0] * n

        for i in range(n):
            local_max = 0
            for j in range(i):
                local_max = max(local_max, height[j])
            max_before[i] = local_max

        for i in range(n - 1, -1, -1):
            local_max = 0
            for j in range(i + 1, n):
                local_max = max(local_max, height[j])
            max_after[i] = local_max

        result = 0

        for i in range(n):
            water_level = min(max_before[i], max_after[i])
            if water_level > height[i]:
                result += water_level - height[i]

        return result