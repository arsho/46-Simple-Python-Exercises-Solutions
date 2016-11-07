'''
Define a function reverse()that computes the reversal
of a string. For example, reverse("I am testing")
should return the string "gnitset ma I".
'''

def reverse(string):
    length = len(string)
    ab = ''
    for i in range(length):
        ab += string[length-1]
        length -= 1
    return ab

print(reverse("I am testing"))
