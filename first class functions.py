#firstclass functions:
# point: when a language looks a function as an object,it is where it will supports first class functions.

def myf1(x):
    return x + 2
def myf2(x):
    return x ** 2
def myf3(x):
    return x // 2

def fc_function(func,x):
    return func(x)
print(fc_function(myf1,8))
# output:10
print(fc_function(myf2,8))
# output:64
print(fc_function(myf3,8))
# output:4
