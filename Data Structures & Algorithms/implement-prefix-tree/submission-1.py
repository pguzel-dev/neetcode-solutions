class TrieNode:
    def __init__(self):
        # no need to include the actual content of the node,
        # instead use a structure like children["a"] where content is the key
        self.children = {}
        self.endWord = False

class PrefixTree:
    def __init__(self):
        # once we have an empty root we basically started the trie so we can just leave it here
        # we can again use the key structure with hashmap on this node for ease of use
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root # start from the top

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        
        current.endWord = True 

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.endWord
        
    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
        