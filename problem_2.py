'''
Statement:
======================
Define a function max_of_three() that takes three numbers as arguments and returns the largest of
them.
'''

def max_of_three(num1, num2, num3):
    if ((not isinstance(num1,int)) and (not isinstance(num1,float))) or ((not isinstance(num2,int)) and (not isinstance(num2,float))) or ((not isinstance(num3,int)) and (not isinstance(num3,float))):
        raise TypeError("All three parameters should be integer or float.")
    max_num = num1
    if(num2>max_num):
        max_num = num2
    if(num3>max_num):
        max_num = num3
    return max_num
    #return max(num1,max(num2,num3))
    
print(max_of_three(36,-366,900))
