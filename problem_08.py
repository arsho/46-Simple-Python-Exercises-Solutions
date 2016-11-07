'''
Define a function is_palindrome()that recognizes
palindromes (i.e. words that look the same written
backwards). For example, is_palindrome("radar")
should return True
'''

def is_palindrome(string):
    ab = ''
    length = len(string)
    for i in range(length):
        ab += string[length-1]
        length -= 1
    if string == ab:
        return True
    else:
        return False


print(is_palindrome("radar"))
print(is_palindrome("abcde"))
