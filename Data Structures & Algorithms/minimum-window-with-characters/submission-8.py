class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = {}

        best_length = float("inf")
        best_left = 0

        req_len = len(need)
        form_len = 0

        left = 0

        for right in range(len(s)):
            char = s[right]

            have[char] = have.get(char, 0) + 1

            # this character is needed and we now have exactly enough of it 
            if char in need and have[char] == need[char]:
                form_len += 1
            
            # move left pointer, cut excess
            while req_len <= form_len:
                window_len = right - left + 1

                if window_len <= best_length:
                    best_length = window_len
                    best_left = left
                
                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    form_len -= 1
                
                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]

        