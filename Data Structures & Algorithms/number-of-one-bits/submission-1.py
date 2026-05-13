# Time: O(log n)
# Space: O(log n)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()