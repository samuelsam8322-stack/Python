# Examples of built-in module:

# 1. math module:
#           used for mathematical operations.
#    basic:   
import math
print(math.sqrt(25))        # square root
print(math.pow(3,5))        # power
print(math.factorial(4))    # factorial value
#    rounding:
print(math.ceil(4.5))       # takes upper(add 1)value.
print(math.floor(8.4))      # Removes the float value.

# 2. random module:
#          used to generate a random values.

# 2.1 random():
import random
print(random.random())              # returns a random float between 0 & 1.

# 2.2 randint(a,b):
print(random.randint(0,10))         # returns a random integer between a & b

# 2.3 randrange(start, stop, step);
print(random.randrange(0,15,3))     # returns a random number from a range.

# 2.4 choice(sequence):
mylist = ["aaa","bbb","ccc","ddd"]
print(random.choice(mylist))        # selects a random element.

# 2.5 shuffle(list):
num = [11,12,13,14,15]
random.shuffle(num)
print(num)                          # shuffle elements in a list.

# 2.6 uniform(a,b):
print(random.uniform(1.6,6.8))      # returns a random floats between a & b.

# examples:

import random
print("Random number:", random.randint(1,100))

names = ["Alice","John","Charlie"]
print("Winner:",random.choice(names))


# 3.collection module():
# It offers advanced data structures like:
# Counting items
# Grouping data
# Fast insert/remove operations
# Structured records

# types:

# 1. Counter():  Used to count frequency of elements.
from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
c = Counter(data)
print(c)

# 2. defaultdict(): Avoids KeyError by giving default values
from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
d['b'] += 2
print(d)

# 3. deque (Double-ended queue): Fast insert/delete from both ends.
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)

# 4. namedtuple(): Tuple with named fields (more readable).
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age'])
s = Student('Samuel', 22)
print(s.name)

# 5.OrderedDict(): Maintains insertion order
from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2
print(d)

# 6. ChainMap(): Combines multiple dictionaries.
from collections import ChainMap

d1 = {'a': 1}
d2 = {'b': 2}
c = ChainMap(d1, d2)
print(c['b'])

# 3. DATETIME MODULE:
#      The datetime module in Python is used to work with dates, times, and time intervals.
# It’s very important for data analysis, logging, and automation tasks.

# What is datetime module?
#  The datetime module provides classes to handle:
#       Date (year, month, day)
#       Time (hour, minute, second)
#       Date + Time together
#       Time differences

# Main Classes in datetime
#     Class	                Description

#   date	            Only date (YYYY-MM-DD)
#   time	            Only time (HH:MM:SS)
#   datetime	        Date + Time
#   timedelta     	    Difference between dates


# 1. Get current date and time
from datetime import datetime

tday = datetime.today()
print(tday)


# 2. Get only date:
from datetime import date

today = date.today()
print(today)


# 3. Create custom date:
from datetime import date

d= date(2026,4,5)
print (d)

# 4. Create custom time:
from datetime import time

t = time(14,30,45)
print(t)

# 5. Working with Date & Time
from datetime import datetime

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)

# 6.Format Date
from datetime import datetime

now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# 7.Convert String to Date
from datetime import datetime
 
date_str = "2026-04-05"
date_obj = datetime.strptime(date_str,"%Y-%m-%d")
print(date_obj)

# Time Difference (timedelta)
# 8. Add / Subtract Days
from datetime import datetime,timedelta

now = datetime.now()

future = now + timedelta(days = 5)
past = now - timedelta(days = 3)

print(future)
print(past)

# 9.Difference between dates:

from datetime import datetime

d1 = datetime(2024,4,5)
d2 = datetime(2026,4,5)

diff = d2-d1
print(diff)
 
