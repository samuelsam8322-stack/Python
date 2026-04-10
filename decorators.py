# DECORATOR:
#       A Decorator function in python is a way to modify or extend the behaviour of another funtion
# without changing itss actual code, It's commonly used for things like 
#      * logging       * authentication

#       A decorator wraps a function inside another function @ symbol is used to denote a 
# decoratot function.

def greet():
    print("Hello")

def add_feature(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

greet = add_feature(greet)
greet()

# Using Decorator Syntax (@)

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()

# Decorator with Arguments
def my_decorator(func):
    def wrapper(name):
        print("Welcome")
        func(name)
    return wrapper

@my_decorator
def greet(name):
    print("Hello", name)

greet("Sam")

# Using *args and **kwargs
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        return func(*args, **kwargs)
    return wrapper


# Real Example: Timing Function
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken:", end - start)
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Done")

slow_function()

