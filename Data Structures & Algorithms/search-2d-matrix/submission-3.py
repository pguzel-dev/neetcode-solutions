# Third direct idea
# Time: 
# Extra space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        bottom, top = 0, (len(matrix)) * (len(matrix[0])) - 1
        while bottom <= top:
            mid = bottom + ((top - bottom) // 2)

            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                top = mid-1

            elif matrix[row][col] < target:
                bottom = mid+1
            
        return False