'''
Write a program that maps a list of words into a list
of integers representing
the lengths of the correponding words
'''

def map_word_length(word_list):
    word_length = [len(single_word) for single_word in word_list]
    word_map = dict(zip(word_list,word_length))
    return word_map

word_list = ['abc','defgh','pqrstuvw']
word_map = map_word_length(word_list)
print(word_map)
