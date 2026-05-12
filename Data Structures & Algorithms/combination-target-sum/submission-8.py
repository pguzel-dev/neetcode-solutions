# Time: O(2^(target / min(nums)))
# Space: O(target / min(nums)) extra space
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        curr = []

        def backtrack(i):
            # Base cases, to stop paths
            if sum(curr) == target:
                results.append(curr.copy())
                return
            if sum(curr) > target:
                return
            if i == len(nums):
                return
            
            # tracking
            curr.append(nums[i])    # add curr num
            backtrack(i)            # reuse in next
            curr.pop()              # take out curr num
            backtrack(i + 1)        # skip out curr num
            i += 1                  # iterate to next num

        backtrack(0)
        return results