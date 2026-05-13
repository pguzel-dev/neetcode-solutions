# Time: O(1)
# Space: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            bit = ((n >> i) & 1)
            if bit == 1:
                res = res | (1 << (31 - i))

        return res