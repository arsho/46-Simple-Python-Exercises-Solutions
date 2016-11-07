'''
Statement:
======================
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the
numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1,
2, 3, 4]) should return 24.
'''
def sum(num_list):
    total = 0
    for c in num_list:
        total+=c
    return total

def multiply(num_list):
    total = 1
    for c in num_list:
        total*=c
    return total

print(sum([1,2,3,4]))
print(multiply([1,2,3,4]))
