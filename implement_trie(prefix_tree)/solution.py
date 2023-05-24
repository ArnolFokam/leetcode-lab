class Node:
    def __init__(self):
        self.children = {}
        self.has_end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        tmp = self.root

        for c in word:
            if c not in tmp.children:
                tmp.children[c] = Node()
            
            tmp = tmp.children[c]

        tmp.has_end = True
        

    def search(self, word: str) -> bool:
        tmp = self.root

        for c in word:
            if c not in tmp.children:
                return False

            tmp = tmp.children[c]

        return True if tmp.has_end else False
        

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root

        for c in prefix:
            if c not in tmp.children:
                return False

            tmp = tmp.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)