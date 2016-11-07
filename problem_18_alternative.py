'''
A pangram is a sentence that contains all the letters of
the English alphabet at least once, for example: The
quick brown fox jumps over the lazy dog. Your
task here is to write a function to check a sentence to
see if it is a pangram or not
'''

def check_pangram(passed_string):
    passed_string = passed_string.lower()
    char_set = set(passed_string)
    letter_list = [c for c in char_set if c.isalpha()]
    return len(letter_list)==26

test_string1 = "The quick brown fox jumps over the lazy dog."
test_string2 = "This line has not all 26 characters. Okay?"
print(check_pangram(test_string1))
print(check_pangram(test_string2))
