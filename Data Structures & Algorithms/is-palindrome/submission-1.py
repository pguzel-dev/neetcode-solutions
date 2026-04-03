class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            char = char.lower()
            if char.isalnum():
                string += char
        if string == string[::-1]:
            return True

        return False
