# scope: a variable is only available from inside the region it is created,python has two 
# scopes:local and global one.
# LOCAL SCOPE:means that a variable created inside a function can only be used inside that function.
# def myf():
#     num = 150
#     print(num)
# myf()
# output:150

#GLOBAL SCOPE:A VARIABLE CREATED OUTSIDE OF A FUNCTION IS GLOBAL AND CAN BE USED INSIDE AND OUTSIDE A FUNCTION.
# num = 150
# def myf():
#     print(f'print1:{num}')
# myf()
# print(f'print2:{num}')
# ouytput:rint1:150
# output:print2:150
#function scope priority is to local scope,it means the local scope will be printed first then the global one will be printed.

# USE GLOBAL KEYWORD:(if you use it,the variable blongs to the global scope)
# num = 1500
# def myf():
#     global num
#     num = 150
# myf()
# print(num)
# output:150
