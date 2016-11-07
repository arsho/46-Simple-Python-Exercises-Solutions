'''
Write a program that maps a list of words into a list
of integers representing
the lengths of the correponding words
'''

def count(list_var):
    value = []
    for i in list_var:
        count = 0
        for j in i:
            count += 1
        value.append(count)
    return value

ab = ['abc','defgh','pqrstuvw']
print(count(ab))
