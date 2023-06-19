closure:is an inner function that has access to  variables of the local scope of outterfunction,evenif it is finished/run.
def outter():
    msg = "hi"
    def inner():
        name = input("enter your name : ")
        print(msg ,name)
    return inner
myf = outter()
myf()
# output:
# enter your name : ALEX
# hi ALEX

def outter(lst):
    def inner():
        for x in lst:
            if x > 6:
                print(x)
        else:
            print("the rest is less than 6")
    return inner
ls = [1,2,4,6,8,122]
myf = outter(ls)
myf()
# output:
# 8
# 122
# the rest is less than 6
