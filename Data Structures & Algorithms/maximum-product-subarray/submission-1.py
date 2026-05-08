class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_res = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]


        for number in nums[1:]:
            local_max = curr_max * number
            local_min = curr_min * number

            curr_max = max(local_max, number , local_min)
            curr_min = min(local_max, number , local_min)

            max_res = max(max_res, curr_max)
        return max_res