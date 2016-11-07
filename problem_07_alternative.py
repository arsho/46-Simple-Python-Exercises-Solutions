'''
Define a function reverse()that computes the reversal
of a string. For example, reverse("I am testing")
should return the string "gnitset ma I".
'''

def reverse(passed_string):
    passed_string_length = len(passed_string)
    reverse_string = ''
    for i in range(passed_string_length-1,-1,-1):
        reverse_string += passed_string[i]
    return reverse_string

print(reverse("I am testing"))
