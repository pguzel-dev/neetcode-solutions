class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            if num - 1 not in seen:
                current = num
                local_long = 1

                while current + 1 in seen:
                    current += 1
                    local_long += 1

                longest = max(longest, local_long)

        return longest