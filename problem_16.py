"""
Write a function filter_long_words()that takes
a list of words and an integer
n and returns the list of words that are longer than n
"""
import unittest


def filter_long_words(words, n):
    gt = []
    for x in words:
        if len(x) > n:
            gt.append(x)
    return gt


def filter_long_words_alternative_1(words, n):
    return [word for word in words if len(word) > n]


def filter_long_words_alternative_2(words, n):
    return list(filter(lambda word: len(word) > n, words))


class TestFilterLongWord(unittest.TestCase):
    def setUp(self):
        self.input_list_1 = ['abc', 'defgh', 'pqrstuvw', '', 'abdghtfd']
        self.input_length_1 = 5
        self.expected_solution_1 = ['pqrstuvw', 'abdghtfd']

    def test_filter_long_words(self):
        self.assertEqual(
            filter_long_words(self.input_list_1, self.input_length_1),
            self.expected_solution_1
        )

    def test_filter_long_words_alternative_1(self):
        self.assertEqual(
            filter_long_words_alternative_1(self.input_list_1,
                                            self.input_length_1),
            self.expected_solution_1
        )

    def test_filter_long_words_alternative_2(self):
        self.assertEqual(
            filter_long_words_alternative_2(self.input_list_1,
                                            self.input_length_1),
            self.expected_solution_1
        )


if __name__ == "__main__":
    unittest.main()
