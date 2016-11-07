'''
Define a function is_palindrome()that recognizes
palindromes (i.e. words that look the same written
backwards). For example, is_palindrome("radar")
should return True
'''

def is_palindrome(passed_string):
    return passed_string==passed_string[::-1]

print(is_palindrome("radar"))
print(is_palindrome("abcde"))
