'''
Statement:
======================
Define a word list that has two index. A variable is_palindrome takes the elements of the list and reverse 
each elements by using [::-1] and the join method turns the list into desired output: "stressed desserts"
'''

word = ['stressed','desserts']
is_palindrome = " ".join(word[::-1])
print(is_palindrome)
