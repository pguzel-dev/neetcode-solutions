# Time Complexity: O(log10(n)) == O(1)
# Space Complexity: O(log10(n)) == O(1)
class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        sign = -1 if x < 0 else 1
        digits = list(str(abs(x)))

        left = 0
        right = len(digits) - 1

        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1

        reversed_num = sign * int("".join(digits))

        if reversed_num < MIN or reversed_num > MAX:
            return 0

        return reversed_num