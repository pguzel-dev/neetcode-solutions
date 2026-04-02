class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            ordered = tuple(sorted(word))
            if ordered not in seen:
                seen[ordered] = []

            seen[ordered].append(word)
        
        return list(seen.values())