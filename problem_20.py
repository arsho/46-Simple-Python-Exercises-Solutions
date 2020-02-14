'''
Represent a small bilingual lexicon as a Python dictionary
in the following fashion {"merry":"god", "christmas":"jul",
"and":"och", "happy":gott", "new":"nytt", "year":"år"}
and use it to translate your Christmas cards from
English into Swedish. That is, write a function
translate()that takes a list of
English words and returns a list of Swedish words
'''
import unittest

word_map = {"merry": "god", "christmas": "jul", \
            "and": "och", "happy": "gott", "new": "nytt", "year": "år"}


def translate_to_swedish(english_words):
    return [word_map.get(k) if word_map.get(k) else k for k in english_words]


class TestTranslate(unittest.TestCase):
    def test_get_song_99_bottles_of_beer(self):
        expected_words = ["god", "jul", "dear"]
        english_words = ["merry", "christmas", "dear"]
        translated_words = translate_to_swedish(english_words)
        number_of_lines = len(translated_words)
        self.assertEqual(
            number_of_lines, 3
        )
        self.assertEqual(
            translated_words, expected_words
        )


if __name__ == "__main__":
    unittest.main()
