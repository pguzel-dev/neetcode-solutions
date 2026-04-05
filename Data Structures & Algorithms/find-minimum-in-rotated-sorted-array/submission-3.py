# Suggested Solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # preserves candidates via res
        left, right = 0, len(nums) - 1

        while left <= right:
            # check if already sorted or not
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
        
            # Check nums[mid], it might be the minimum
            mid = (left + right) // 2
            res = min(res, nums[mid])

            # determines which side is sorted
            if nums[mid] >= nums[left]:
                # Left half is sorted
                left = mid + 1
            else:
                # We are in the rotated part
                right = mid - 1

        return res