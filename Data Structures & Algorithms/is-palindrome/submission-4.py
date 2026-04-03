class Solution:
    def is_alphanum(self, c: str) -> bool:
        return (
            ord("a") <= ord(c) <= ord("z") or
            ord("A") <= ord(c) <= ord("Z") or
            ord("0") <= ord(c) <= ord("9")
        )
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.is_alphanum(s[left]):
                left += 1
            while left < right and not self.is_alphanum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True