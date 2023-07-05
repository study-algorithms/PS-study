class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordCompleted = False

class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.head
        for ch in word:
            if ch not in currNode.children:
                currNode.children[ch] = TrieNode()
            currNode = currNode.children[ch]
        currNode.isWordCompleted = True

    def search(self, word: str) -> bool:
        currNode = self.head
        for ch in word:
            if ch not in currNode.children:
                return False
            currNode = currNode.children[ch]
        return currNode.isWordCompleted

    def startsWith(self, prefix: str) -> bool:
        currNode = self.head
        for ch in prefix:
            if ch not in currNode.children:
                return False
            currNode = currNode.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
