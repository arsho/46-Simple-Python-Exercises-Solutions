'''
Define a procedure histogram() that takes a list of
integers and prints a histogram to the screen.
For example, histogram([4, 9, 7])should print the following:

****
*********
*******
'''

def histogram(list_var):
    s='\n'.join(['*'*i for i in list_var])
    return s

print(histogram([4, 9, 7]))
    
