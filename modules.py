# MODULES:
#       A Module in python is simply a file containing python code (function, variables, classes)
#  that you can reuse in other programs.
# mymodule.py
def greet():
    print("Hello")

# import mymodule():
# mymodule.greet()

# TYPES :

# 1. Built- in module :
#           These are pre-installed with python, you don't need to install them.
#        * math
#        * sys
#        * os
import math
print(math.sqrt(16))


# 2. User-defined module:
#           These are modules created by the user.
#        * myfile.py


# 3. External (Third party) module:
#           These are not built-in. You need to install them using pip
#        * numpy - numercial computing
#        * pandas - data analysis
#        * requests - HTTP requests

#       pip install numpy

# Ways to import module:
import math              # import whole numbers
import math as m         # alias
from math import sqrt    # import specific function

# why we use module:
#  * reuse code
#  * organize large programs
#  * avoid repetition
#  * readability


