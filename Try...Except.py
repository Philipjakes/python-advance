# try ...except:for handling errors,pay attention to the case sensitive.
# try:
#     get_number = int(input(" enter any number :"))
#     get_number1 = int(input(" enter any number :"))
# except ValueError:
#     print("wrong input")
# output:
#  enter any number :2
#  enter any number :w
# wrong input
# point:you must type the system error after the except.

# to define many exception you must define system error alternatively:
# try:
#     get_number = int(input(" enter any number :"))
#     get_number1 = int(input(" enter any number :"))
# except ValueError:
#     print("wrong input")
# except TypeError:
#     print("wrong type")
# finally:
#     print("finished")
# output:
#  enter any number :2
#  enter any number :r
# wrong input
# finished

# try:
#     get_number = int(input(" enter any number :"))
#     get_number1 = int(input(" enter any number :"))
# except ValueError:
#     print("wrong input")
# except TypeError:
#     print("wrong type")
# else:
#     print("finished")
# # output:

# using alias: 
# try:
#     get_number = int(input(" enter any number :"))
#     get_number1 = int(input(" enter any number :"))
# except ValueError:
#     print("wrong input")
# except TypeError as t:
#     print(t)
# else:
#     print("finished")
# output:
# enter any number :2
#  enter any number :q
# wrong input

x = "handle"
# if get_number<get_number1:
#      raise Exception("get_number is smaller than get_number1")
 # output: raises an error.
#  OR:
if type(x) is not int:
    raise TypeError("only integers")