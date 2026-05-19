# Time: O(n)
# Space: O(1)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            nums.append(nums[idx])
        return nums

        