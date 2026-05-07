class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0

        for money in nums:
            new_best = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = new_best

        return prev1