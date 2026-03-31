#Built-in functions():
#       built-in function are functions that are already provided by a programming language.so you 
# can use them directly without writing their definitions youself.
#   For examples:
""" print(), input(), len(), type(), int(), float(), str(), sum(), max(), min(),
    range(), abs(), round(), all(), any(), sorted(), reversed().
"""

# map function():
#           The map() function in python is used to apply a function to every item
# in an iterable (like a list, tuple,etc) and return a map object ( which is an iterator).
#           map (function,iterable)

numbers = [ 1, 2, 3, 4]
def square(a):
    return a *a 
result = map (square,numbers)
print(list(result))

# lambda function():
num = [2,3,4,5]
myData = map (lambda x:x*x, num)
print(list(myData))

# filter function():        (where the condition is true for the specific condition.)
#        The filter function() in python is used to select ( filter out) elements from
#  an iterable based on a condition.
#           filter(function,iterable)
 
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = filter(is_even, numbers)

print(list(result))  

# reduce function ():
#       The reduce() function in python is used to apply a function cumulatively to 
# the items of an iterable, reducing it to single value.

from functools import reduce

#reduce(function, iterable)


from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)
print(result)  