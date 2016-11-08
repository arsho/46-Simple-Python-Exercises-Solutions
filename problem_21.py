'''
 Write a function char_freq()that takes a string and
 builds a frequency listing of the characters contained
 in it. Represent the frequency listing as a Python
 dictionary. Try it with something like
 char_freq("abbabcbdbabdbdbabababcbcbab")
 '''

def char_freq(passed_string):
    char_freq_dic = dict()
    for c in passed_string:
        if c in char_freq_dic.keys():
            char_freq_dic[c]=char_freq_dic.get(c)+1
        else:
            char_freq_dic[c]=1
    char_sorted_dic = sorted(char_freq_dic.items())
    return char_sorted_dic

print(char_freq("abbabcGDAbdbabdbdbababajsdhfdgfjsgfygbcbcbab"))
    
