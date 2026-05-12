# Time: O(n * 2^n)
# Space: O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                results.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return results