'''
Write a function filter_long_words()that takes
a list of words and an integer
n and returns the list of words that are longer than n
'''

def filter_long_words(word_list,n):
    return [word for word in word_list if len(word)>n]

word_list = ['abc','defgh','pqrstuvw','','abdghtfd']
print(filter_long_words(word_list,5))
