class Solution:    
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s) -> bool:
            return s == s[::-1]
        
        results = []
        part = []

        def dfs(index):
            if index >= len(s):
                results.append(part.copy())
                return
            
            for j in range(index, len(s)):
                if isPalindrome(s[index:j+1]):
                    part.append(s[index:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return results