class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solutions = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            solutions[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            solutions[i] *= postfix
            postfix *= nums[i]

        return solutions