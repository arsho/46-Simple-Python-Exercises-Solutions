'''
A pangram is a sentence that contains all the letters of
the English alphabet at least once, for example: The
quick brown fox jumps over the lazy dog. Your
task here is to write a function to check a sentence to
see if it is a pangram or not
'''

def pangram(string):
    string = string.lower()
    alphabet = ['a','b','c','d','e','f','g','h',\
                'i','j','k','l','m','n','o','p',\
                'q','r','s','t','u','v','w','x','y','z']

    a = 0
    for i in alphabet:
        if i not in string:
            print("it's not a pangram")
            a = 5
            break
    
    if a != 5:
        print("it's a pangram")

ab = "The quick brown fox jumps over the lazy dog."
pangram(ab)
