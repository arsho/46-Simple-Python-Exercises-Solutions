'''
Implement the higher order functions map(), filter()and reduce().
(They are built-in but writing them yourself
may be a good exercise.
'''
from functools import reduce
def mymap(func,element_list):
    return [func(element) for element in element_list]

element_list = ["this","test","sdk","fingerprint scanner"]
print(mymap(len,element_list))
#The following is the default map
#print(list(map(len,element_list)))

def check_odd(a):
    return a%2==1

def myfilter(func, element_list):
    return [element for element in element_list if func(element)==True]

element_list = [21,343,32,11,46]
print(myfilter(check_odd,element_list))
#The following is the default filter
#print(list(filter(check_odd,element_list)))

def add(a,b):
    return a+b

def myreduce(func, element_list):
    if len(element_list)==0:
        return 0
    else:
        result = element_list[0]
        for i in range(1,len(element_list)):
            result=func(result,element_list[i])
        return result

element_list = [1,2,3,4,5,6]
print(myreduce(add,element_list))
#The following is the default reduce
#print(reduce(add,element_list,0))
