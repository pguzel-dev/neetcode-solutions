class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber1(loot):
            prev2 = 0
            prev1 = 0

            for money in loot:
                new_best = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = new_best

            return prev1

        if len(nums) == 1:
            return nums[0]

        return max(
            houseRobber1(nums[1:]),
            houseRobber1(nums[:-1])
        )