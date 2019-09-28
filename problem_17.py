'''
Write a version of a palindrome recognizer that
also accepts phrase palindromes such as "Go hang a
salami I'm a lasagna hog.", "Was it a rat I
saw?", "Step on no pets", "Sit on a potato pan,
Otis", "Lisa Bonet ate no basil",
"Satan, oscillate my metallic sonatas", "I roamed under
it as a tired nude Maori", "Rise to vote sir", or the
exclamation "Dammit, I'm mad!". Note that
punctuation, capitalization, and spacing are usually ignored
'''
import unittest


def palindrome(line):
    line = line.lower().replace(" ", "")
    tem = ['.', ',', '!', '?', '\"', "\'"]
    for i in tem:
        line = line.replace(i, "")
    reverse_line = ''
    line_length = len(line)
    for i in range(line_length - 1, -1, -1):
        reverse_line += line[i]
    return line == reverse_line


def palindrome_alternative_1(line):
    line = "".join(filter(str.isalpha, line.lower()))
    return line == line[::-1]


def palindrome_alternative_2(line):
    line = ''.join([c for c in line.lower() if c.isalnum()])
    return line == line[::-1]


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.test_cases = (
            {
                "input_str": "Go hang a salami I'm a lasagna hog.",
                "expected_output": True
            },
            {
                "input_str": "Was it a rat I saw?",
                "expected_output": True
            },
            {
                "input_str": "Step on no pets",
                "expected_output": True
            },
            {
                "input_str": "Sit on a potato pan, Otis",
                "expected_output": True
            },
            {
                "input_str": "Lisa Bonet ate no basil",
                "expected_output": True
            },
            {
                "input_str": "Satan, oscillate my metallic sonatas",
                "expected_output": True
            },
            {
                "input_str": "I roamed under it as a tired nude Maori",
                "expected_output": True
            },
            {
                "input_str": "Rise to vote sir",
                "expected_output": True
            },
            {
                "input_str": "Dammit, I'm mad!",
                "expected_output": True
            },
            {
                "input_str": "This is no palindrome!",
                "expected_output": False
            },
        )

    def test_palindrome(self):
        for test_case in self.test_cases:
            self.assertEqual(
                palindrome(test_case["input_str"]),
                test_case["expected_output"]
            )

    def test_palindrome_alternative_1(self):
        for test_case in self.test_cases:
            self.assertEqual(
                palindrome_alternative_1(test_case["input_str"]),
                test_case["expected_output"]
            )

    def test_palindrome_alternative_2(self):
        for test_case in self.test_cases:
            self.assertEqual(
                palindrome_alternative_2(test_case["input_str"]),
                test_case["expected_output"]
            )


if __name__ == "__main__":
    unittest.main()
