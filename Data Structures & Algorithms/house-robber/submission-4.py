class Solution:
    def rob(self, nums: List[int]) -> int:
        # Best amount we can rob up to the house before the previous one
        best_two_houses_back = 0

        # Best amount we can rob up to the previous house
        best_previous_house = 0

        for money in nums:
            # Option 1: skip this house, keep previous best
            skip_current = best_previous_house

            # Option 2: rob this house, add best from two houses back
            rob_current = best_two_houses_back + money

            # Best amount after considering this house
            best_current_house = max(skip_current, rob_current)

            # Shift forward for the next house
            best_two_houses_back = best_previous_house
            best_previous_house = best_current_house

        # Best amount after considering all houses
        return best_previous_house