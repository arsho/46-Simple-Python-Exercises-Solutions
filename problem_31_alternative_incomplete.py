'''
Implement the higher order functions map(), filter()and reduce().
(They are built-in but writing them yourself
may be a good exercise.
'''

def mymap(func,element_list):
    return [func(element) for element in element_list]

element_list = ["this","test","sdk","fingerprint scanner"]
print(mymap(len,element_list))

