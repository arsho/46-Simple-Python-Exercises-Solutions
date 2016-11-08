'''
Write a program that maps a list of words into a list of
integers representing the lengths of the correponding words.
Write it in three different ways:
1) using a for-loop,
2) using the higher order function map()
3) using list comprehensions
'''


def size_of_words_1(list_a):
    size = []
    for item in list_a:
        count = 0
        for i in item:
            count += 1          # no need extra for loop
        size.append(count)     # could be .append(len(item))
    return size


#####################################################

def size_of_words_2(list_b):
    def size(string):
        count = 0
        for i in string:
            count += 1      # no need extra function
        return count        # shortcut - map(len,list_b)
    return list(map(size ,list_b))  # only map doesn't work
                                    # list(map(f,seq))

#####################################################
##### List comprehension is new to me, gd shortcut :)

def size_of_words_3(list_c):
    return [len(item) for item in list_c]



ab = ['mithila','prokriti','amrita']
print(size_of_words_1(ab))
print(size_of_words_2(ab))
print(size_of_words_3(ab))
