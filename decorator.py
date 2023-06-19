# decoratores:allow us to add something to our function with no changes on it.
# def decorate(original_f):
#     def wrapper():
#         print("this is the first step,")
#         return original_f
#     return wrapper
# @decorate
# def originalfunction():
#     print("this is a decorator.")
# re = originalfunction()
# re()
# output:
# this is the first step,
# this is a decorator.

# def myg(original_function):
#     def wrapper():
#         print('hello')
#         return original_function
#     return wrapper
# @myg
# def function():
#     print(f"hi",input("enter your name : "))
# re = function()
# re()
# output:
# hello
# enter your name: sara
# hi sara
# in the example above,if the return of original function has had a (),in the decorated function
# you should call the function in the simple way(function()),if  return of the original function
# has no ()or has not been called,you should modify the decorated function(res = function(),res())

def myg(original_function):
    def wrapper(list):
        print(list)
        return original_function
    return wrapper
@myg
def function():
    for i in ls:
        x = i*2
        print(x)
ls = [1,3,5,7,9]
    
re = function(ls)
re()
 