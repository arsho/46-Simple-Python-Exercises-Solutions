'''
A pangram is a sentence that contains all the letters of
the English alphabet at least once, for example: The
quick brown fox jumps over the lazy dog. Your
task here is to write a function to check a sentence to
see if it is a pangram or not
'''
import unittest
import string


def pangram(line):
    line = line.lower()
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', \
                 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', \
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in alphabets:
        if i not in line:
            return False
    return True


def pangram_alternative_1(line):
    line = line.lower()
    alphabets = string.ascii_lowercase
    for i in alphabets:
        if i not in line:
            return False
    return True

def pangram_alternative_2(line):
    line = line.lower()
    char_set = set(line)
    letters = [c for c in char_set if c.isalpha()]
    return len(letters)==26


class TestPangram(unittest.TestCase):
    def setUp(self):
        self.test_cases = (
            {
                "input_str": "The quick brown fox jumps over the lazy dog.",
                "expected_output": True
            },
            {
                "input_str": "Was it a rat I saw?",
                "expected_output": False
            },
            {
                "input_str": "Step on no pets",
                "expected_output": False
            },
            {
                "input_str": "Sit on a potato pan, Otis",
                "expected_output": False
            },
            {
                "input_str": "Lisa Bonet ate no basil",
                "expected_output": False
            },
            {
                "input_str": "Satan, oscillate my metallic sonatas",
                "expected_output": False
            },
            {
                "input_str": "I roamed under it as a tired nude Maori",
                "expected_output": False
            },
            {
                "input_str": "Rise to vote sir",
                "expected_output": False
            },
            {
                "input_str": "Dammit, I'm mad!",
                "expected_output": False
            },
            {
                "input_str": "This is no palindrome!",
                "expected_output": False
            },
        )

    def test_pangram(self):
        for test_case in self.test_cases:
            self.assertEqual(
                pangram(test_case["input_str"]),
                test_case["expected_output"]
            )

    def test_pangram_alternative_1(self):
        for test_case in self.test_cases:
            self.assertEqual(
                pangram_alternative_1(test_case["input_str"]),
                test_case["expected_output"]
            )

    def test_pangram_alternative_2(self):
        for test_case in self.test_cases:
            self.assertEqual(
                pangram_alternative_2(test_case["input_str"]),
                test_case["expected_output"]
            )

if __name__ == "__main__":
    unittest.main()
