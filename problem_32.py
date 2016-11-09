'''
Write a version of a palindrome recogniser
that accepts a file name from the
user, reads each line, and prints the line to the screen
if it is a palindrome
'''

def palindrome(string):
    string = string.lower()    
    string = string.replace(" ","").replace("\n","")   # lines contain '\n'
    tem = ['.',',','!','?','\"',"\'"]                  # in file, need to remove
    for i in tem:
        string = string.replace(i,"")
    tmp=''
    length = len(string)
    for i in range(length):
        tmp += string[length-1]
        length -= 1
    if string == tmp:
        return True
    else:
        return False


print("Enter your filename with extension : ")
file_name = input(">>")
with open(file_name,'r') as f:
    for item in f.readlines():     # readlines() create list 
        print(palindrome(item))     # of all lines till EOF
