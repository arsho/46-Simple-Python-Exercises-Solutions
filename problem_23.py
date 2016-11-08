"""
Define a simple "spelling correction" function correct() that takes a string and
sees to it that
1) two or more occurrences of the space character is compressed into one,
and
2) inserts an extra space after a period if the period is directly followed
by a letter.

E.g. correct("This is very funny and          cool.Indeed!")
should return
"This is very funny and cool. Indeed!"

Tip: Use regular expressions!
"""
import re
def correct(passed_line):
    passed_line = re.sub("\s{2,}"," ",passed_line)
    passed_line = re.sub(r'\.(\w)',r'. \1',passed_line)
    return passed_line

print(correct("This is very funny and          cool.Indeed!okay. bye."))
    
        
