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

def check_palindrome(passed_string):
    passed_string = passed_string.lower()
    passed_string = ''.join([c for c in passed_string if c.isalnum()])
    return passed_string==passed_string[::-1]

test_string1 = "Was it a rat I saw?"
test_string2 = "Step on no pets"
test_string3 = "Not palindrome at all!"

print (check_palindrome(test_string1))
print (check_palindrome(test_string2))
print (check_palindrome(test_string3))

