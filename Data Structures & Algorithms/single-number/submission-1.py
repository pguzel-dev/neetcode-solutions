class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for index in range(len(nums)-2,-1,-1):
            nums[index] = nums[index] ^ nums[index + 1]
        return nums[0]