'''
Write a function filter_long_words()that takes
a list of words and an integer
n and returns the list of words that are longer than n
'''

def filter_long_words(list_var,n):
    gt = []
    for x in list_var:
        if len(x) > n:
            gt.append(x)
    return gt

ab = ['abc','defgh','pqrstuvw','','abdghtfd']
print(filter_long_words(ab,5))
