class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        results = {}

        for string in strs:
            ordered = ''.join(sorted(string))

            if ordered not in seen:
                seen.add(ordered)
                results[ordered] = []

            results[ordered].append(string)

        return list(results.values())