# Personal solution
class TrieNode:
    def __init__(self):
        self.children = {} # a : TrieNode
        self.endWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.endWord = True

    def search(self, word: str) -> bool:
        # recursive func for adequate search on "."
        def dfs(index, node):
            # we got equal word length, check and return
            if index == len(word):
                return node.endWord

            char = word[index]

            # if joker card activate recursive
            if char == ".":
                # try all available children with revursive
                for child in node.children.values():
                    # increase index since its still a char
                    if dfs(index + 1, child):
                        return True
                return False

            # if char not available in children
            if char not in node.children:
                return False

            # recursive again to enable regular search
            return dfs(index + 1, node.children[char])

        return dfs(0, self.root)