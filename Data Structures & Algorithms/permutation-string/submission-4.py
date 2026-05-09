class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        s1sort = sorted(s1)

        while right < len(s2):
            s2sort = sorted(s2[left : right + 1])

            if s1sort == s2sort:
                return True

            left += 1
            right += 1
        
        return False