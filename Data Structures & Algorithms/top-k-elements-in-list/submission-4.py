class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for n, c in counts.items():
            freq[c].append(n)

        res = []

        for bucket in freq[::-1]:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
                    # instead of doing everything,
                    # end when we get to the target