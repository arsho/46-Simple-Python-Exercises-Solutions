'''
Write a program that maps a list of words into a list of
integers representing the lengths of the correponding words.
Write it in three different ways:
1) using a for-loop,
2) using the higher order function map()
3) using list comprehensions
'''


def map_word_with_length_using_for(word_list):
    map_word_length = dict()
    for item in word_list:
        map_word_length[item] = len(item)
    return map_word_length


#####################################################

def map_word_with_length_using_map(word_list):
    word_len_list = list(map(lambda x:len(x),word_list))
    return dict(zip(word_list,word_len_list))

#####################################################

def map_word_with_length_using_list_comprehensions(word_list):
    word_len_list = [len(item) for item in word_list]
    return dict(zip(word_list, word_len_list))


# list of Shanto's imaginary girlfriends :D
word_list = ['mithila','prokriti','amrita'] 
print(map_word_with_length_using_for(word_list))
print(map_word_with_length_using_map(word_list))
print(map_word_with_length_using_list_comprehensions(word_list))
