class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(bottom: int, top: int) -> int:
            if bottom > top:
                return -1

            mid = (bottom + top) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                return binarySearch(bottom, mid-1)

            elif nums[mid] < target:
                return binarySearch(mid+1, top)
            
        return binarySearch(0, len(nums)-1)
