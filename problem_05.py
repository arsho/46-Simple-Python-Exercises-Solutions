'''
Statement:
======================
Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's
language"). That is, double every consonant and place an occurrence of "o" in between. For example,
translate("this is fun") should return the string "tothohisos isos fofunon".
'''
import string
def translate(text):
    if(not isinstance(text, str)):
        raise TypeError("Parameter should be string.")

    all_letter = string.ascii_letters
    vowel_letter = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    constant_letter = [c for c in all_letter if c not in vowel_letter]
    
    output = ""
    for c in text:
        if c in constant_letter:
            output+=c+"o"+c
        else:
            output+=c
    return output
print(translate("this is fun"))
