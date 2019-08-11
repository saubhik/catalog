# Selection Sort
import unittest
from typing import List


def selection_sort(input_list: List):
    for i in range(len(input_list)):
        min_index = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_index] > input_list[j]:
                min_index = j
        input_list[min_index], input_list[i] = input_list[i], input_list[min_index]

    return input_list


class Test(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual([11, 12, 22, 25, 64], selection_sort([64, 12, 22, 25, 11]))
        self.assertEqual([64, 64], selection_sort([64, 64]))
        self.assertEqual([], selection_sort([]))
