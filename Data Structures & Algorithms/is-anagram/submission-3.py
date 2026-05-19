# Time: O(n + m)
# Space: O(n + m)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = {}
        t_seen = {}

        for val in s:
            s_seen[val] = s_seen.get(val, 0) + 1
        for val in t:
            t_seen[val] = t_seen.get(val, 0) + 1
        
        return s_seen == t_seen