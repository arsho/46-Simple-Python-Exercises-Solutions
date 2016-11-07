'''
Define a function overlapping()that takes two lists
and returns True if they have at least one member
in common, False otherwise. You may use your
is_member()function, or the in operator, but for the
sake of the exercise, you should (also) write
it using two nested for-loops
'''

def overlapping(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False

a = [3,4,5,6,7]
b = [6,7,8,9,10]
c = [91,92,93]

print(overlapping(a,b))
print(overlapping(a,c))
