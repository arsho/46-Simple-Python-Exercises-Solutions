'''
Write a function find_longest_word()that takes a
list of words and returns the
length of the longest one
'''


def find_longest_word(word_list):
    word_length = [len(word) for word in word_list]
    return max(word_length)


word_list = ['abc','defgh','pqrstuvw','']
print(find_longest_word(word_list))
