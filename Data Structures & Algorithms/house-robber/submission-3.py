# Time: O(n)
# Space: O(n)
# Recursion with memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
  
        for index in range(len(nums) - 3, -1, -1):
            nums[index] = max(nums[index] + nums[index + 2], nums[index + 1])

        return nums[0]
