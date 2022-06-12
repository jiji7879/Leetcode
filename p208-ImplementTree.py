class Trie:

    def __init__(self):
        self.chartrie = {}

    def insert(self, word: str) -> None:
        if word[0] not in self.chartrie:
            self.chartrie[word[0]] = Trie()
        trie = self.chartrie[word[0]]
        i=1
        while i < len(word):
            if word[i] not in trie.chartrie:
                trie.chartrie[word[i]] = Trie()
            trie = trie.chartrie[word[i]]
            i+=1
        trie.chartrie[" "] = Trie()

    def search(self, word: str) -> bool:
        if word[0] not in self.chartrie:
            return False
        trie = self.chartrie[word[0]]
        i=1
        while i < len(word):
            if word[i] not in trie.chartrie:
                return False
            trie = trie.chartrie[word[i]]
            i+=1
        if " " in trie.chartrie:
            return True

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.chartrie:
            return False
        trie = self.chartrie[prefix[0]]
        i=1
        while i < len(prefix):
            if prefix[i] not in trie.chartrie:
                return False
            trie = trie.chartrie[prefix[i]]
            i+=1
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
