# ITERATORS: is an object that can be iterated upon all the iterable values without considering the data structure.
# HOW TO CREATE AN ITERATOR:you have two ways to create it:first item is to use iter() method and the second one is to use create an iterator class.
# _list = [2,45,2.75,66]
# it = iter(_list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# output:
# 2
# 45
# 2.75
# 66

# _dict = {"name":"alison","age":"14","name1":"albert","age1":"16"}
# it = iter(_dict)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# output:
# name
# age
# name1
# age1

# point:the __iter__ acts similar(initializing,etc.) but you must return both __iter__() and __next__() in the sequence.
# class _iter:
#     def __iter__(self):
#         self.value = 1
#         return self
#     def __next__(self):
#         val = self.value
#         self.value+=1
#         return val
# iterclass = iter(_iter())
# print(next(iterclass))
# print(next(iterclass))
# print(next(iterclass))
# print(next(iterclass))
# output:
# 1
# 2
# 3
# 4

# stop iteration:it is used to prevent the iteration.
class _iter:
    def __iter__(self):
        self.value = 1
        return self
    def __next__(self):
        if self.value < 4:
            val = self.value
            self.value+=1
            return val
        else:
            raise StopIteration
iterclass = iter(_iter())
print(next(iterclass))
print(next(iterclass))
print(next(iterclass))
print(next(iterclass))
# output: raise an error after printing number 3.