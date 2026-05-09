class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            n = len(strs[i])
            strs[i] = str(n) + "@" + strs[i]
        return "".join(strs)
            
    def decode(self, s: str) -> List[str]:
        message = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "@":
                j += 1
            
            length = int(s[i:j])

            word_start = j + 1
            word_end = word_start + length

            message.append(s[word_start:word_end])

            i = word_end
        
        return message



