class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        curr = []

        def backtrack(start):
            if sum(curr) == target:
                results.append(curr.copy())
                return

            if sum(curr) > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                backtrack(i + 1)   # i + 1 because each element can be used once
                curr.pop()

        backtrack(0)
        return results