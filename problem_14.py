"""
Write a program that maps a list of words into a list
of integers representing
the lengths of the corresponding words
"""
import unittest


def map_word_length(words):
    word_lengths = [len(word) for word in words]
    word_map = list(zip(words, word_lengths))
    return word_map


class TestMapWordLength(unittest.TestCase):
    def setUp(self):
        self.input_list_1 = ['abc', 'defgh', 'pqrstuvw']
        self.expected_solution_1 = [('abc', 3), ('defgh', 5), ('pqrstuvw', 8)]
        self.input_list_2 = ['abc', '', 'dummy']
        self.expected_solution_2 = [('abc', 3), ('', 0), ('dummy', 5)]
        self.input_list_3 = []
        self.expected_solution_3 = []

    def test_map_word_length(self):
        self.assertEqual(map_word_length(self.input_list_1),
                         self.expected_solution_1)
        self.assertEqual(map_word_length(self.input_list_2),
                         self.expected_solution_2)
        self.assertEqual(map_word_length(self.input_list_3),
                         self.expected_solution_3)


if __name__ == "__main__":
    unittest.main()
