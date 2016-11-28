'''
Statement:
======================
According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file
name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilapsto the screen.
For example, if "stressed" and "desserts" is part of the word list, the the output should include
the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!
'''
import re
#filename = input("Enter filename: ")
filename = "words.txt"
fin = open(filename,"r")
all_lines = fin.readlines()
word_list = set()
word_dict = dict()
for line in all_lines:
    line = line[:-1].lower()
    words = line.split(" ")
    for word in words:
        word = re.sub("[^a-zA-Z]+", "", word)
        word_list.add(word)
        reverse_word = word[::-1]
        if reverse_word in word_list:
            if reverse_word not in word_dict:
                word_dict[word] = reverse_word

for word in word_dict.keys():
    print(word," ",word_dict[word])
