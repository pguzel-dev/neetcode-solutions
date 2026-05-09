class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = {}

        for char in s1:
            freq_map[char] = freq_map.get(char, 0) + 1

        count = {}
        left = 0

        for right in range(len(s2)):
            count[s2[right]] = count.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                count[s2[left]] -= 1

                if count[s2[left]] == 0:
                    del count[s2[left]]

                left += 1

            if freq_map == count:
                return True

        return False