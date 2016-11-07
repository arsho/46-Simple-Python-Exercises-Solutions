'''
Statement:
======================
Define a function that computes the length of a given list or string. (It is true that Python has the len()
function built in, but writing it yourself is nevertheless a good exercise.)
'''

def custom_len(given_list_or_string):
    if(not isinstance(given_list_or_string, str)) and (not isinstance(given_list_or_string, list)):
        raise TypeError("Parameter should be list or string type")
    cnt = 0
    for elem in given_list_or_string:
        cnt+=1
    return cnt
print(custom_len("asd"))
