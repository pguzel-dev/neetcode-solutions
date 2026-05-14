class Solution:
    def reverse(self, x: int) -> int:
        orgiginal = x
        x = abs(x)
        res = int(str(x)[::-1])
        if orgiginal < 0:
            res *= -1
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return res