# TASK :

# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def my_division(x,y):
    try:
        result = x / y 
        print("result:",result)
    except ZeroDivisionError:
        print("Divison by zero operator is not allowed.")

x = 50
y = 0
my_division(x,y)

# 2.Write a Python program that prompts the user to input an integer and raises a ValueError
# exception if the input is not a valid integer.
try:
    num = int(input("Input a value:"))
    value = num + 10
    print(value)
except ValueError:
    print("Value Error, input a valid integer")

#3.Write a Python program that opens a file and handles a FileNotFoundError
# exception if the file does not exist.
def open_file(filename):
    try:
        file = open(filename,"r")
        contents = file.read
        print(contents)
        file.close()
    except FileNotFoundError:
        print("FileNotFoundError,input a valid filename")

file_name = str(input("Enter a filename:"))
open_file(file_name)

# 4.Write a Python program that prompts the user to input two numbers and raises a TypeError 
# exception if the inputs are not numerical.
def numericals(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except TypeError:
            print("The above given value has TypeError")

num1 = numericals("Enter a value:")
num2 = numericals("Enter a value:")
result = num1 * num2
print("The product of given two numerical value is:",result)

# 5.Write a Python program that opens a file and handles a PermissionError exception
# if there is a permission issue.
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except PermissionError:
        print("Error: Permission denied to open the file.")

file_name = str(input("Input a file name:"))
open_file(file_name)

# 6.Write a Python program that executes an operation on a list and handles an IndexError 
# exception if the index is out of range.

def test_index(data,index):
    try:
        result = data[index]
        print("Results:",result)
    except IndexError:
        print("Error: Index out of range")

nums = [1,2,3,4,5,6]
index = int(input("Input your index:"))
test_index(nums,index)


# 7.Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt 
# exception if the user cancels the input.

try:
    n = int(input("Input a number:"))
    print("Your entered:",n)
except KeyboardInterrupt:
    print("Input cancelled by the user.")

# 8.Write a Python program that executes division and handles an ArithmeticError 
# exception if there is an arithmetic error.
def division(dividend,divisor):
    try:
        result = dividend / divisor
        print("Results:",result)
    except ArithmeticError:
        print("Error: Arithmetic error occured!")

dividend = float(input("Input the Dividend:"))
divisor=float(input("Input the Divisor:"))
division(dividend,divisor)


#9.Write a Python program that opens a file and handles a UnicodeDecodeError exception if there
# is an encoding issue.

def open_file(filename):
    encoding = input("Input the encoding (ASCII, UTF-16, UTF-8) for the file: ")
    try:
        with open(filename, 'r', encoding=encoding) as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except UnicodeDecodeError:
        print("Error: Encoding issue occurred while reading the file.")

file_name = input("Input the file name: ")
open_file(file_name) 


# 10.Write a Python program that executes a list operation and handles an AttributeError
# exception if the attribute does not exist.

def test_list_operation(nums):
    try:
        r = len(nums)  
        print("Length of the list:", r)
    except AttributeError:
        print("Error: The list does not have a 'length' attribute.")

nums = [1, 2, 3, 4, 5]
test_list_operation(nums)


# TASK 2:


# 1.Basic try and except block:
try:
    print(undefined_variable)
except NameError:
    print("This variable is not defined.")

# 2.Handling multiple exceptions
try:
    result = 10 / 0
except (ZeroDivisionError, TypeError) as e:
    print("Error occurred:", str(e))

# 3.Using the else clause in exception handling
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("Result is", result)

# 4.Using the finally clause in exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
finally:
    print("This block of code will always execute.")

# 5.Raising exceptions using raise
try:
    raise ValueError("This is a custom error message.")
except ValueError as e:
    print("An error occurred:", str(e))

# 6. Creating custom exceptions
class CustomError(Exception):
    pass
try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print("An error occurred:", str(e))

# 7.Catching all exceptions using Exception
try:
    result = 10 / 0
except Exception as e:
    print("An error occurred:", str(e))
try:
    print(undefined_variable)
except Exception as e:
    print("An error occurred:", str(e))

# 8. Using assert for exception handling
try:
    x = -1
    assert x >= 0, "Only positive values are allowed."
except AssertionError as e:
    print("An error occurred:", str(e))

# 9.Handling exceptions within functions
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero!")
        return None

print(divide(10, 0))

# 10.Using a while loop for handling exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again…")

# 11.Reraising exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught an exception")
    raise

# 12. Using else clause with try/except inside a function
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
        return None
    else:
        print("Division successful!")
        return result
print(divide(10, 2))

# 13.Handling exceptions with finally clause in file handling
try:
    f = open('myfile.txt', 'r')
    content = f.read()
    f.close()
except IOError:
    print('File not found.')

# 14. Ignoring exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    pass

# 15.Propagating exceptions
def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    else:
        return x ** 0.5    
try:
    print(sqrt(-10))
except ValueError as e:
    print("An error occurred:", str(e))

