class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        best = ""

        for left in range(len(s)):
            have = Counter()

            for right in range(left, len(s)):
                have[s[right]] += 1

                valid = True
                for ch in need:
                    if have[ch] < need[ch]:
                        valid = False
                        break

                if valid:
                    current = s[left:right + 1]

                    if best == "" or len(current) < len(best):
                        best = current

                    break

        return best