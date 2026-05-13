# Time: O(1)
# Space: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            bit = (n >> i) & 1 # Get the bit at position i
            res = res | (bit << (31 - i)) # Place it at the reversed position

        return res