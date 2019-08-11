# Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/
#

import unittest
from typing import Dict


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = dict()
        self.end: bool = False


class WordDictionary:
    def __init__(self):
        """
        Initialize data structure
        """
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """
        Adds a word into the data structure.
        :param word: the word to add.
        :return: None
        """
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
        current_node.end = True

    def search(self, word: str, current_node: TrieNode = None) -> bool:
        """
        Returns if the word is in the data structure.
        A word could contain the dot character "." to represent any one letter.
        :param word: the word to search for.
        :param current_node: current node the trie we start searching from.
        :return: True or False.
        """
        if not current_node:
            current_node = self.root

        if not word:
            return current_node.end

        if word[0] in current_node.children:
            return self.search(word[1:], current_node.children[word[0]])

        if word[0] != ".":
            return False

        for key in current_node.children:
            if self.search(word[1:], current_node.children[key]):
                return True

        return False


class Test(unittest.TestCase):
    def test_add_word(self):
        word_dict = WordDictionary()
        word_dict.add_word("dog")
        self.assertEqual(True, word_dict.search("dog"))
        self.assertEqual(False, word_dict.search("dogs"))

    def test_search(self):
        word_dict = WordDictionary()
        word_dict.add_word("dog")
        word_dict.add_word("mad")
        self.assertEqual(True, word_dict.search("dog"))
        self.assertEqual(False, word_dict.search("..e"))
        self.assertEqual(True, word_dict.search("..d"))
        self.assertEqual(True, word_dict.search(".a."))
        self.assertEqual(False, word_dict.search(".p."))


if __name__ == "__main__":
    unittest.main()
