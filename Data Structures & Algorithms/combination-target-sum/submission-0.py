class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(index: int, current: List[int], total: int) -> None:
            # Found a valid combination
            if total == target:
                results.append(current.copy())
                return
            
            # Stop if we run out of numbers or go over target
            if index >= len(nums) or total > target:
                return

            # Include nums[index]
            current.append(nums[index])
            dfs(index, current, total + nums[index])  # reuse same number
            current.pop()  # backtrack

            # Skip nums[index]
            dfs(index + 1, current, total)

        dfs(0, [], 0)
        return results