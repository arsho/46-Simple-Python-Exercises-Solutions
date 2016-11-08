"""
In cryptography, a Caesar cipher is a very simple encryption
techniques in which each letter in the plain text is
replaced by a letter some fixed number of
positions down the alphabet. For example, with a shift of 3,
A would be replaced by D, B would become E, and so on.
The method is named after Julius Caesar, who used it to
communicate with his generals. ROT-13 ("rotate
by 13 places") is a widely used example of a Caesar cipher
where the shift is 13. In Python, the key for ROT-13 may
be represented by means of the following dictionary:

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

Your task in this exercise is to implement an encoder/
decoder of ROT-13. Once you're done, you will be able to
read the following secret message:

Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!

Note that since English has 26 characters, your ROT-13 program
will be able to both encode and decode texts written in English.
"""
import string
lowercase_normal = list(string.ascii_lowercase)
lowercase_encode = [chr(((ord(c)+13-ord('a'))%26)+ord('a')) for c in lowercase_normal]
uppercase_normal = list(string.ascii_uppercase)
uppercase_encode = [chr(((ord(c)+13-ord('A'))%26)+ord('A')) for c in uppercase_normal]

def ROT_13_encoder(passed_string):
    encoder_map=dict(zip(lowercase_normal,lowercase_encode)).copy()
    encoder_map.update(dict(zip(uppercase_normal,uppercase_encode)))
    output_string = ''
    for c in passed_string:
        output_string+=encoder_map.get(c,c)
    return output_string

def ROT_13_decoder(passed_string):
    decoder_map=dict(zip(lowercase_encode,lowercase_normal)).copy()
    decoder_map.update(dict(zip(uppercase_encode,uppercase_normal)))
    output_string = ''
    for c in passed_string:
        output_string+=decoder_map.get(c,c)
    return output_string

print(ROT_13_encoder(ROT_13_decoder('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')))
print(ROT_13_decoder('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))
    
        
