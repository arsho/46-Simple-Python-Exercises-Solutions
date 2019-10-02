'''
"99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips,
as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's
simple lyrics are as follows:
99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.
The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or
singers reach zero.
Your task here is write a Python program capable of generating all the verses of the song
'''
import unittest


def get_song_99_bottles_of_beer():
    n = 99
    song = []
    for i in range(n, 0, -1):
        quantity = ""
        if i > 1:
            quantity = "s"
        song.append("{current} bottle{quantity} of beer on the wall, " \
                    "{current} bottle{quantity} of beer.".format(current=i,
                                                                 quantity=quantity))
        if i - 1 > 1:
            quantity = "s"
        song.append("Take one down, pass it around, " \
                    "{decrease} bottle{quantity} of beer on the wall.".format(
            decrease=i - 1,
            quantity=quantity))
    return song


class TestSong(unittest.TestCase):
    def test_get_song_99_bottles_of_beer(self):
        expected_first_line = "99 bottles of beer on the wall, 99 bottles of beer."
        expected_last_line = "Take one down, pass it around, 0 bottle of beer on the wall."
        song = get_song_99_bottles_of_beer()
        number_of_lines = len(song)
        self.assertEqual(
            number_of_lines, 198
        )
        self.assertEqual(
            song[0], expected_first_line
        )
        self.assertEqual(
            song[-1], expected_last_line
        )


if __name__ == "__main__":
    unittest.main()
