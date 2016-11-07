'''
The function max()from exercise 1) and the function
max_of_three()from exercise 2) will only work for
two and three numbers, respectively. But
suppose we have a much larger number of numbers,
or suppose we cannot tell in advance how many
they are? Write a function max_in_list()that takes a
list of numbers and returns the largest one
'''

def a(listname):
    length = len(listname)
    tmp = []
    for i in range(0,length-1):
        maximum = max(listname[i],listname[i+1])
        tmp.append(maximum)
    return tmp  

def max_in_list(abc):
    if len(abc) == 1:
        return abc[0]
    else:
        return max_in_list(a(abc))

ab = [3,7,98,34,12,14]
print(max_in_list(ab))
    


######################################################
###################### shortcut ######################
######################################################

def maximum(list_var):
    list_var.sort()
    return list_var[-1]
print(maximum(ab))
