'''
Write a function find_longest_word()that takes a list of
words and returns the length of the longest one.
Use only higher order functions
'''

def find_longest_word(list_a):
    return max(list(map(lambda x:len(x),list_a)))

ab = ['sadswesdf','cat','meaow','to','asdeqw']
print(find_longest_word(ab))
