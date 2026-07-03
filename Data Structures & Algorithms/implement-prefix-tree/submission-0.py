class PrefixTree:

    def __init__(self):
        self.map = collections.defaultdict(set)

    def insert(self, word: str) -> None:
        for r in range(0, len(word)):
            self.map[word[:r + 1]].add(word)


    def search(self, word: str) -> bool:
        for words in self.map.values():
            if word in words:
                return True
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.map:
            return True
        else:
            return False
        
        