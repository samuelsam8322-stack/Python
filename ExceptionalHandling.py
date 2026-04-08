# Exceptional Handling:
#           Exceptional handling in python is the process of responding to the occurrance
# of exceptions ( exceptions are unwanted conditions the distrubs the program execution)
# it occurred.


# Types of Error:

# 1. Syntax error:
#       syntax error (or parsing error) occur when the code violates the formal rules
# of the python language. These are caught by the interpreter before the program starts
# running.
#               * Indentation error
#               * Tab error
#               * General syntax error

# 2. Runtime error:
#       These occur while the program is executing. even if the syntax is correct. Python
# uses 'exception' to signal these issuees. Which can be handled using 'try...except...

#Common Types of Runtime Errors

# ZeroDivisionError:        Attempting to divide a number by zero.
# NameError:                Using a variable or function name that has not been defined.
# TypeError:                Performing an operation on incompatible data types 
#                           (e.g., adding a string to an integer).
# IndexError:               Accessing a list or tuple index that is out of its range.
# KeyError:                 Attempting to access a dictionary key that does not exist.
# FileNotFoundError:        Trying to open or access a file that is missing or at the wrong path.
# RecursionError:           A recursive function calls itself too many times without hitting a base case.
# RuntimeError (Generic):   A specific built-in exception raised when an error occurs that doesn't 
#                           fall into any other defined category. 

# How to handle runtime errors with core keywords :

# * try        - wraps the code that might cause an error.
# * except     - contains the code that executes if an exception occurs in the 'try' block
#                you can catch specific exceptions( eg: except value error) or multiple
#                exception in a tuple ( eg:except(value error,type error)
# * else       - Runs only if no exceptions were raised in the 'try' block.
# * finally    - always executes, regardless of whatever  exception occurred, making
#                it ideal for cleanup tasks like closing.


# 3. Logical error:
#           logical errors(or semantics error) are the most difficults to detects because
# the program runs without crashing but produces incorrect results.


# Differents between Errors and Exceptions:

# Error      :Issues in the program logic such as SYNTAX ERROR, etc., it occurrs at 
#            compile time.
# Exceptions :Problems that occurs at runtime and can be managed using exception handling
#             (eg: invalid input, missing files).


# Types of runtime error:

# 1. ZeroDivisionError
x = 10 / 0

# 2.NameError - Occurs when a variable is not defined.
print(a)   

# 3.TypeError - Occurs when operations are performed on incompatible types.
x = "10" + 5

# 4.ValueError - Occurs when a function gets the correct type but invalid value.
int("abc")

# 5.IndexError - Occurs when accessing an invalid index in a list.
lst = [1, 2, 3]
print(lst[5])

# 6.KeyError -Occurs when accessing a non-existing key in a dictionary.
d = {"a": 1}
print(d["b"])

# 7.AttributeError - Occurs when an invalid attribute is used.
x = 10
x.append(5)

# 8.ImportError - Occurs when a module cannot be imported.
import non_existing_module

# 9.FileNotFoundError - Occurs when a file is not found.
open("file.txt")

# 10.OverflowError - Occurs when a number exceeds limits.
import math
math.exp(1000)



# Example Handling Runtime Error
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")