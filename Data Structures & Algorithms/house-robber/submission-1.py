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

            cache[index] = max(dfs(index + 1), dfs(index + 2) + nums[index])
            return cache[index]
        
        return max(dfs(0), dfs(1))
