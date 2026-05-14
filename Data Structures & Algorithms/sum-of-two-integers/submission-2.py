# Time: O(1)
# Space: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # -1
        max_int = 0x7FFFFFFF # largest positive 32-bit signed integer

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)