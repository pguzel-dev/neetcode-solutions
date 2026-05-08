class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Best product found anywhere so far
        max_res = nums[0]

        # Best/worst product ending at the current position
        curr_max = nums[0]
        curr_min = nums[0]

        for number in nums[1:]:
            # Extend previous best/worst with current number
            local_max = curr_max * number
            local_min = curr_min * number

            # Best product ending here: extend or start fresh
            curr_max = max(local_max, number, local_min)

            # Worst product ending here, needed for negative flips
            curr_min = min(local_max, number, local_min)

            # Update global best answer
            max_res = max(max_res, curr_max)

        return max_res