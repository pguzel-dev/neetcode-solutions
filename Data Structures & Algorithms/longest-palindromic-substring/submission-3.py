# Time: O(n^2)
# Space: O(1)
# 1st solution, just with extra explanation
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Expand outward from a given center and return the palindrome found
        def expand(left: int, right: int) -> str:
            # Keep expanding while bounds are valid and chars match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            # Return the valid palindrome after overshooting by one step
            return s[left + 1:right]

        longest = ""

        # Try every index as a possible palindrome center
        for i in range(len(s)):
            # Odd-length palindrome, centered on one character
            odd = expand(i, i)

            # Even-length palindrome, centered between two characters
            even = expand(i, i + 1)

            # Update longest if the odd palindrome is better
            if len(odd) > len(longest):
                longest = odd
            
            # Update longest if the even palindrome is better
            if len(even) > len(longest):
                longest = even

        return longest