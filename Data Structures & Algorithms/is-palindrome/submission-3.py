class Solution:
    def is_alphanum(self, c: str) -> bool:
        return (
            "a" <= c <= "z" or
            "A" <= c <= "Z" or
            "0" <= c <= "9"
        )
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not self.is_alphanum(s[left]):
                left += 1
                continue
            if not self.is_alphanum(s[right]):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True