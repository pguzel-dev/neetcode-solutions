# Time: O(n)
# Space: O(n)
# Recursion with memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
  
        def dfs(index: int):
            if index >= len(nums):
                return 0

            if cache[index] != -1:
                return cache[index]

            cache[index] = max(nums[index] + dfs(index + 2), dfs(index + 1))
            return cache[index]
        
        return max(dfs(0), dfs(1))
