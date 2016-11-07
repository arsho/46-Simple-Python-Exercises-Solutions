'''
Write a function find_longest_word()that takes a
list of words and returns the
length of the longest one
'''


def countmax(list):
    value = []
    for i in list:
        value.append(len(i))
    value.sort()
    return value[-1]


ab = ['abc','defgh','pqrstuvw','']
print(countmax(ab))
