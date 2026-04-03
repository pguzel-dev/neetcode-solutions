class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphanum(c):
            return (
                "a" <= c <= "z" or
                "A" <= c <= "Z" or
                "0" <= c <= "9"
            )

        left = 0
        right = len(s) - 1

        while left < right:
            if not is_alphanum(s[left]):
                left += 1
                continue
            if not is_alphanum(s[right]):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True