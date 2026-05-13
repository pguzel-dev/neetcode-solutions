# Time: O(2^n)
# Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(index: int, value: List[int]):
            if index >= len(value):
                return 0
            
            if index in cache:
                return cache[index]

            skip_curr = dfs(index + 1, value)
            rob_curr = value[index] + dfs(index + 2, value)
            cache[index] = max(skip_curr, rob_curr)
            return cache[index]
        
        cache = {}
        first_cut = dfs(0, nums[:-1])
        cache = {}
        second_cut = dfs(0, nums[1:])
        
        return max(first_cut, second_cut)