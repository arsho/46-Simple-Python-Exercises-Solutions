'''
Write a version of a palindrome recognizer that
also accepts phrase palindromes such as "Go hang a
salami I'm a lasagna hog.", "Was it a rat I
saw?", "Step on no pets", "Sit on a potato pan,
Otis", "Lisa Bonet ate no basil",
"Satan, oscillate my metallic sonatas", "I roamed under
it as a tired nude Maori", "Rise to vote sir", or the
exclamation "Dammit, I'm mad!". Note that
punctuation, capitalization, and spacing are usually ignored
'''

def palindrome(string):
    string = string.lower()    #only string.lower won't work
    string = string.replace(" ","")  #must be contained in 
    tem = ['.',',','!','?','\"',"\'"]   #variable  :)
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

ab = "Was it a rat I saw?"
print (palindrome(ab))
