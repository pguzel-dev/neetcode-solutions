# First direct idea
# Time: O(mn)
# Extra space: O(mn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [x for arr in matrix for x in arr]

        bottom, top = 0, len(nums)-1
        while bottom <= top:
            mid = bottom + ((top - bottom) // 2)

            if nums[mid] == target:
                return True

            elif nums[mid] > target:
                top = mid-1

            elif nums[mid] < target:
                bottom = mid+1
            
        return False