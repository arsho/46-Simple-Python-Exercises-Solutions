'''
Statement:
======================
Define a function max()  that takes two numbers as arguments and returns the largest of them. Use the if­
then­else construct available in Python. (It is true that Python has the max()  function built in, but writing it
yourself is nevertheless a good exercise.)
'''

def max(num1,num2):
    if ((not isinstance(num1,int)) and (not isinstance(num1,float))) or ((not isinstance(num2,int)) and (not isinstance(num2,float))):
        raise TypeError("Both parameters should be integer or float.")
    if num1>num2:
        return num1
    else:
        return num2
print(max(3,69))
