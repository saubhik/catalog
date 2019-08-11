# Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/
#
# A trie is also known as radix or prefix tree.

import unittest


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        Complexity:
            space: O(n)
            time : O(n)
            where n is the number of characters in the word.
        :param word: the word to insert.
        :return: None
        """
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        Complexity:
            space: O(1)
            time : O(n)
            where n is the number of characters in the word.
        :param word: the word to search for.
        :return: True or False, depending on existence of the word in the trie.
        """
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.end

    def starts_with(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        Complexity:
            space: O(1)
            time : O(n)
            where n is the number of characters in prefix.
        :param prefix: the prefix to search for.
        :return: True or False.
        """
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True


class Test(unittest.TestCase):
    def test_trie_insert(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(True, trie.search("apple"))
        del trie

    def test_trie_search(self):
        trie = Trie()
        trie.insert("apple")
        trie.insert("apples")
        self.assertEqual(False, trie.search("app"))
        self.assertEqual(False, trie.search("ap"))
        self.assertEqual(True, trie.search("apple"))
        self.assertEqual(True, trie.search("apples"))
        del trie

    def test_trie_starts_with(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(True, trie.starts_with("app"))
        self.assertEqual(True, trie.starts_with("apple"))
        self.assertEqual(False, trie.starts_with("apples"))
        del trie


if __name__ == "__main__":
    unittest.main()
