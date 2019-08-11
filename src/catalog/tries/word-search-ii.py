# Word Search II
#
# https://leetcode.com/problems/word-search-ii/
#

import unittest
from typing import List


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
        current_node.end = True


class WordSearch:
    @staticmethod
    def _is_valid(i, j, board):
        return 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] != "#"

    def _find_words_at(
        self,
        i: int,
        j: int,
        board: List[List[str]],
        trie_node: TrieNode,
        output: List[str],
        current_word: str,
    ):
        if trie_node.end:
            output.append(current_word)
            # unset end flag to not encounter this word again
            trie_node.end = False

        letter_ij = board[i][j]
        # trick to mark visited board positions
        board[i][j] = "#"

        if self._is_valid(i, j + 1, board):
            letter = board[i][j + 1]
            if letter in trie_node.children:
                self._find_words_at(
                    i,
                    j + 1,
                    board,
                    trie_node.children[letter],
                    output,
                    current_word + letter,
                )

        if self._is_valid(i + 1, j, board):
            letter = board[i + 1][j]
            if letter in trie_node.children:
                self._find_words_at(
                    i + 1,
                    j,
                    board,
                    trie_node.children[letter],
                    output,
                    current_word + letter,
                )

        if self._is_valid(i - 1, j, board):
            letter = board[i - 1][j]
            if letter in trie_node.children:
                self._find_words_at(
                    i - 1,
                    j,
                    board,
                    trie_node.children[letter],
                    output,
                    current_word + letter,
                )

        if self._is_valid(i, j - 1, board):
            letter = board[i][j - 1]
            if letter in trie_node.children:
                self._find_words_at(
                    i,
                    j - 1,
                    board,
                    trie_node.children[letter],
                    output,
                    current_word + letter,
                )

        board[i][j] = letter_ij

    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:

        output = list()

        # create a trie from words
        trie = Trie()
        for word in words:
            trie.insert(word)

        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter in trie.root.children:
                    self._find_words_at(
                        i, j, board, trie.root.children[letter], output, letter
                    )

        return output


class Test(unittest.TestCase):
    def test_find_words_1(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        words = ["oath", "pea", "eat", "eath", "rain"]
        word_search = WordSearch()
        self.assertEqual(
            {"eat", "oath", "eath"}, set(word_search.find_words(board, words))
        )

    def test_find_words_2(self):
        board = [["a", "a"]]
        words = ["a"]
        word_search = WordSearch()
        self.assertEqual({"a"}, set(word_search.find_words(board, words)))


if __name__ == "__main__":
    unittest.main()
