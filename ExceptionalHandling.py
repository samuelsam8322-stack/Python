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