class TrieNode:
    def __init__(self):
        self.children = {}
        self.has_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:

        tmp = self.root

        for c in word:
            if c not in tmp.children:
                tmp.children[c] = TrieNode()

            tmp = tmp.children[c]
        
        tmp.has_end = True
        

    def search(self, word: str) -> bool:

        def dfs(j, root):
            tmp = root
            
            for i in range(j, len(word)):
                c = word[i]
                
                if c == '.':
                    for child in tmp.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in tmp.children:
                        return False
                    tmp = tmp.children[c]
                    
            return tmp.has_end
        
        return dfs(0, self.root)