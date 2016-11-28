'''
Statement:
======================
Write a program that given a text file will
create a new text file in which all the lines from the original file are
numbered from 1 to n (where n is the number of lines in the file)
'''


#filename = input("Enter a line: ")
filename = "test.txt"
output_filename = "test_numbered.txt"
fin = open(filename,"r")
fout = open(output_filename,"w")
lines = fin.readlines()
word_dict = dict()
cnt = 0
for line in lines:
    cnt+=1
    output_line = str(cnt)+". "+line
    fout.write(output_line)

print("Lines are numbered. Check: "+output_filename)
fin.close()
fout.close()
