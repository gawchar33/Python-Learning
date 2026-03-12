'''reduce() is a function from the functools module used to apply a function
cumulatively to the items of an iterable, reducing the entire
list into a single value.'''

from functools import reduce
num=3,4,5,5
def add(a,b):
    return a+b
result=[]
result=reduce(add,num)
print(result)