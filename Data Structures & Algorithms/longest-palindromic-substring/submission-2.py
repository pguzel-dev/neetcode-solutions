class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Stores the longest palindrome found so far
        res = ""

        # Stores the length of the longest palindrome
        resLen = 0

        # Try every index as a possible center
        for i in range(len(s)):
            # Check odd-length palindromes, centered at i
            l, r = i, i

            # Expand while bounds are valid and chars match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update result if this palindrome is longer
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                # Expand outward
                l -= 1
                r += 1

            # Check even-length palindromes, centered between i and i + 1
            l, r = i, i + 1

            # Expand while bounds are valid and chars match
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Update result if this palindrome is longer
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                # Expand outward
                l -= 1
                r += 1

        # Return longest palindrome found
        return res