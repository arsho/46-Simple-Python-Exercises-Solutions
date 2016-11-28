'''
Statement:
======================
A hapax legomenon (often abbreviated to hapax) is a word which occurs
only once in either the written
record of a language, the works of an author,
or in a single text. Define a function that given the file name of
a text will return all its hapaxes.
Make sure your program ignores capitalization.'''

import re
#filename = input("Enter a line: ")
filename = "words.txt"
fin = open(filename,"r")
lines = fin.readlines()
word_dict = dict()
for line in lines:
    word_list = re.findall('\w+',line)
    for word in word_list:
        word = word.lower()
        if word in word_dict:
            word_dict[word]=word_dict[word]+1
        else:
            word_dict[word]=1

for word in word_dict:
    if word_dict[word] == 1:
        print(word)
