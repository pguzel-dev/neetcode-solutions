# Second direct idea
# Time: 
# Extra space:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
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