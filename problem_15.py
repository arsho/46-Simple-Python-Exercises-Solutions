'''
Write a function find_longest_word()that takes a
list of words and returns the
length of the longest one
'''
import unittest


def find_longest_word(words):
    lengths = []
    for i in words:
        lengths.append(len(i))
    return sorted(lengths, reverse=True)[0]


def find_longest_word_alternative(words):
    return max([len(word) for word in words])


class TestFindLongestWord(unittest.TestCase):
    def setUp(self):
        self.input_list_1 = ['abc', 'defgh', 'pqrstuvw', '']
        self.expected_solution_1 = 8
        self.input_list_2 = ['', '', '', '']
        self.expected_solution_2 = 0

    def test_find_longest_word(self):
        self.assertEqual(find_longest_word(self.input_list_1),
                         self.expected_solution_1)
        self.assertEqual(find_longest_word(self.input_list_2),
                         self.expected_solution_2)

    def test_find_longest_word_alternative(self):
        self.assertEqual(find_longest_word_alternative(self.input_list_1),
                         self.expected_solution_1)
        self.assertEqual(find_longest_word_alternative(self.input_list_2),
                         self.expected_solution_2)


if __name__ == "__main__":
    unittest.main()
