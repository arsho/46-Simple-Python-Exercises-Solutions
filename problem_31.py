'''
Implement the higher order functions map(), filter()and reduce().
(They are built-in but writing them yourself
may be a good exercise.
'''

def mymap(func,seq):
    ini = []
    for item in seq:
        ini.append(func(item))
    return ini

def myfilter(func,seq):
    ini = []
    for item in seq:
        if func(item)==True:
            ini.append(item)
    return ini

def myreduce(func,seq):
    i = len(seq)
    while i>1:
        f = func(seq[0],seq[1])
        seq.pop(0)                  # "del seq[0]" do so
        seq.pop(0)
        seq.insert(0,f)
        i = len(seq)
    return seq[0]


### Copied from net

def myreduce_net(func, seq):
    tmp = seq[0]
    for item in seq[1:]:      # works with only 'seq' too
        tmp = func(tmp,item)
    return tmp

print(mymap(len,['abc','abcd']))
print(myfilter(lambda x:x>5,[1,3,5,7,9]))
print(myreduce(lambda a,b:a if a>b else b,[3,7,4,5,1]))
print(myreduce_net(lambda a,b:a if a>b else b,[3,7,4,5,1]))
