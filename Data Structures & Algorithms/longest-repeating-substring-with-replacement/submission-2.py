# Devised solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # Dict
        left = 0
        longest = 0 # Longest valid substring found
        max_freq = 0 # Most frequent character in the current window

        for right in range(len(s)):
            # Add/update current character on freq map
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # (window length - most frequent char count) > k
            while ((right - left) - max_freq >= k):
                # Remove the leftmost character from the window
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest