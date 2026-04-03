class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len_seq = 0

        for i in range(len(nums)):
            current = nums[i]
            len_seq = 1

            while True:
                next_found = False
                for j in range(len(nums)):
                    if nums[j] == current + 1:
                        next_found = True
                        current += 1
                        len_seq += 1
                        break
                if not next_found:
                    break

            max_len_seq = max(max_len_seq, len_seq)

        return max_len_seq
