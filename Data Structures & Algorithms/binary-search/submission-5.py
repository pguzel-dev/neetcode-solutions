class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom, top = 0, len(nums)-1
        while not bottom > top:
            mid = (bottom + top) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                bottom, top = bottom, mid-1

            elif nums[mid] < target:
                bottom, top = mid+1, top
            
        return -1