from typing import List, Optional


class Trie:
    def __init__(self):
        """
        Initialize an empty trie.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if the prefix is a prefix of any word in the trie, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

    def load(self, words: List[str]) -> None:
        """ """
        for word in words:
            self.insert(word)

    def __repr__(self) -> str:
        raise NotImplementedError()