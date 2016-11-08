'''
Using the higher order function filter(), define a function
filter_long_words()that takes a list of words and an integer
n and returns the list of words that are longer than n
'''

def filter_long_words(list_a,n):
    return list(filter(lambda x:len(x)>n, list_a))

ab = ['abc','abcd','abcde','abcdef']
print(filter_long_words(ab,4))
