# practice sol
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for string in strs:
            ordered = ''.join(sorted(string))

            if ordered not in seen.keys():
                seen[ordered] = []

            seen[ordered].append(string)

        return list(seen.values())