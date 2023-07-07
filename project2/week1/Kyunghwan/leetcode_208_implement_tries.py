class Trie:

    def __init__(self):
        self.t = []
        

    def insert(self, word: str) -> None:
        self.t.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.t:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        for target in self.t:
            if target.startswith(prefix, 0):
                return True
        return False
    

a = Trie