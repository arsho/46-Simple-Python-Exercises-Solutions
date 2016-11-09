'''
Write a function char_freq()that takes a string and builds a
frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary.
Try it with something like
char_freq("abbabcbdbabdbdbabababcbcbab")
'''

import collections
def char_freq(string):
    return sorted(collections.Counter(list(string)).items())

print(char_freq("abbabcbdbabdbdbabababcbcbab"))
