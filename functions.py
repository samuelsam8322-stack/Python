# Functions:
# Function is a block of code that performs a specific task.
# It defined using the def keyword.

def f1():
    print("Function is working")
f1()

# Arguements :
#    it is the actual value passed to the function when its called.
# Parameters:
#    it is variable in a function's definition that acts as a placeholder for 
#    data its expects to receive.

def add (a,b):     #  Parameters
    c= a+b
    print(c)

add(10,20)        # Arguements

# Scopes in python:
#         Scopes refers to the accessibility and visibility of the variable.

# TYPES OF SCOPES:  LEGB

# 1. lOCAL SCOPE: * variables defined inside the function
#                 * Accessible only within the function.
def localscope():
    x = 100
    print(x)

localscope()


# 2.ENCLOSING SCOPE: * Applies to the nested function (function inside the function)
#                    * inner functions can access variable from the outer(Enclosing)function.
def outer():
    x= 20
    def inner():
        print(x)

    inner()

outer()


# 3.GLOBAL SCOPE: * variables defined at the top level of a script or module.
#                 * accessible throughout the file.

n1 =600
def data():
    print(n1)

data()

# To Modify a global variable inside a funcrtion,use "global"
x= 5
def data():
    global x
    x = 10
    print(x,"Inside the function")

data()
print(x,"Outside a function")



# TYPES OF FUNCTION:

# Built-in Function:  predifined functions available in python .no need to defined them.
#                    eg : len(),type(),sum(),....etc
# User-defined Function: fuctions created using def.
#                    eg:  def greet():
#                            print("Hello!")
#                         greet()


# Arbitary Argements (*argue):
#        used when you don't know how many positional arguements will be passed.
#        collected into a tuple().
#    eg:
def myData (*a):
    print(a)

myData(10,20,30,40,50)

def f1 (c,*a):
    print(a)
    print(c)

f1 (1,2,3,4,5)