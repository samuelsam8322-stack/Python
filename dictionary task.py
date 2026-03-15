# 1.Count Frequency of Elements Given a list, create a dictionary that stores the frequency of each element.
numbers = [1,2,2,3,3,3,4]
freq = {}
for i in numbers:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1
print(freq)

# 2.Find Key with Maximum Value Write a program to find the key with the highest value in a dictionary {"a":10, "b":25, "c":15}.
d = {"a":10, "b":25, "c":15}
max_key = ""
max_value = 0
for i in d:
    if d[i] > max_value:
        max_value = d[i]
        max_key = i
print('the highest value is:', max_key)

# 3.Merge two dictionaries into one d1 = {"a":1, "b":2} d2 = {"c":3, "d":4}.
d1 = {"a":1, "b":2}
d2 = {"c":3, "d":4}
d1.update(d2)
print(d1)

# 4.Invert a Dictionary {"a":1,"b":2,"c":3} Swap keys and values.
d = {"a":1, "b":2, "c":3}
new_dict = {}
for i in d:
    new_dict[d[i]] = i
print(new_dict)

# 5.Remove duplicate values from a dictionary {"a":10,"b":20,"c":10,"d":30}.
d = {'a':10, 'b':20, 'c':10, 'd':30}
new_dict = {}
for i in d:
    if d[i] not in new_dict.values():
        new_dict[i] = d[i]
print(new_dict)

# 6.Group Words ["cat","dog","elephant","bat","tiger"] by Length Create a dictionary that groups words by their length.
words = ["cat","dog","elephant","bat","tiger"]
result = {}
for i in words:
    l = len(i)
    if l not in result:
        result[l] = [i]
    else:
        result[l].append(i)
print(result)

# 7.Sort Dictionary by Values Sort a dictionary {"a":3,"b":1,"c":2} based on values.
d = {'a':3,'b':1,'c':2}
# dictionary to list
items = list(d.items())
items.sort(key=lambda x: x[1])
# list to dictionary
new_dict = dict(items)
print(new_dict)

# 8.Find Common Keys in Two Dictionaries  {"a":1,"b":2,"c":3} , {"b":20,"c":30,"d":40}.
d1 = {"a":1,"b":2,"c":3}
d2 = {"b":20,"c":30,"d":40}
common = []
for i in d1:
    if i in d2:
        common.append(i)
print(common)

# 9.Write a program to find the sum of all values in dictionary {"a":10,"b":20,"c":30}.
d = {"a":10, "b":20, "c":30}
total = 0
for i in d:
    total = total + d[i]
print(total)

# 10.Create a dictionary using two lists keys = ["a","b","c"] values = [10,20,30].
keys = ["a","b","c"]
values = [10,20,30]
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)