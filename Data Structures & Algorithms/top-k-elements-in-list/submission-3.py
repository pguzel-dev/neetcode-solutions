class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for n, c in counts.items():
            freq[c].append(n)
        
        res = []

        for array in freq[::-1]:
            if not array:
                continue
            for each in array:
                res.append(each)

        return res[:k]