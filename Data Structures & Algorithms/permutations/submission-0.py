class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        curr = []

        def backtrack():
            if len(curr) == len(nums):
                results.append(curr.copy())
                return
            
            for num in nums:
                if num in curr:
                    continue
                curr.append(num)
                backtrack()
                curr.pop()
        
        backtrack()
        return results
