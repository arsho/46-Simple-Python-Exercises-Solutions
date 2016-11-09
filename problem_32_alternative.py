'''
Write a version of a palindrome recogniser
that accepts a file name from the
user, reads each line, and prints the line to the screen
if it is a palindrome
'''
import re
def check_palindrome(test_line):
    test_line = test_line[:-1]
    modify_line = test_line.lower()
    # removing all non alpha numeric character using regex
    modify_line = re.sub(r"\W+","",modify_line) 
    if modify_line==modify_line[::-1]:
        return test_line
    return False


print("Enter your filename with extension: ",end="")
file_name = input()
try:
    with open(file_name,'r') as f:
        for line in f.readlines():     # readlines() create list 
            check_val = check_palindrome(line)
            if check_val != False:
                print(check_val)
except:
    print(str(file_name)+" not found")
