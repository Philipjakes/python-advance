# generators:an easiest way of the iterators.
def my_gen(x):
    for gen in range(x):
        yield gen
x = my_gen(4)
print(next(x))
print(next(x))
print(next(x))
# output:
# 0
# 1
# 2