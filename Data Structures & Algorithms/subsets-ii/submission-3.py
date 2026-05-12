# Time: O(n * 2^n)
# Space: O(n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        curr = []

        def backtrack(start):
            results.append(curr.copy())

            # no need to check for smt like
            # if start >= len(nums): return
            # since the for loop itself acts as the base case
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()

        backtrack(0)
        return results