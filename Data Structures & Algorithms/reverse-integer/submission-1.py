# Time Complexity: O(log10(n))
# Space Complexity: O(1)
import math

class Solution:
    def reverse(self, x: int) -> int:
        # Reverse a signed 32-bit integer.
        # Return 0 if the reversed value goes outside this range:
        # [-2147483648, 2147483647]

        MIN = -2147483648  # -2^31
        MAX = 2147483647   #  2^31 - 1

        res = 0

        while x:
            # Get the last digit.
            # math.fmod handles negative numbers the way we want.
            digit = int(math.fmod(x, 10))       # (python dumb) -1 % 10 = 9

            # Remove the last digit.
            # int(x / 10) truncates toward 0.
            x = int(x / 10)                     # (python dumb) -1 // 10 = -1

            # Check positive overflow before updating res.
            if (
                res > MAX // 10 or # whether multiplying res by 10 and adding digit would overflow past MAX.
                (res == MAX // 10 and digit >= MAX % 10)
            ):
                return 0

            # Check negative overflow before updating res.
            if (
                res < MIN // 10 or
                (res == MIN // 10 and digit <= MIN % 10)
            ):
                return 0

            # Append digit to the reversed result.
            res = (res * 10) + digit

        return res