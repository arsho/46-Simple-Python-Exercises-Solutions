'''
Write a function find_longest_word()that takes a list of
words and returns the length of the longest one.
Use only higher order functions
'''

def find_longest_word(list_a):
    return max(list(map(len,list_a)))

ab = ['cat','meaow','to']
print(find_longest_word(ab))
