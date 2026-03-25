# Dictionary Task:
# 1.Write a program to find largest value d = {"a":10, "b":50, "c":30}.
d = {"a":10, "b":50, "c":30}
lar_value = max(d.values())
print("The largest value:",lar_value)

# 2.Write a program to count total values greater than 20 d = {"a":10, "b":25, "c":30, "d":5}.
d = {"a":10, "b":25, "c":30, "d":5}
count = 0
for i in d.values():
    if i > 20:
        count += 1
print("The total values greater than 20:",count)

# 3.Write a program to create a new dictionary with squared values d = {"a":2, "b":3, "c":4}.
d = {"a":2, "b":3, "c":4}
squared_dict = { k : v**2 for k,v in d.items()}
print("Squared dictionary:",squared_dict)

# 4.write a program to find smallest value d = {"a":10, "b":5, "c":30}.
d = {"a":10, "b":5, "c":30}
value = min(d.values())
print("The smallest value:",value)

# 5.Write a program to find key with maximum value d = {"a":10, "b":50, "c":30}.
d = {"a":10, "b":50, "c":30}
max_key = max(d.keys())
print("The key with maximum value:",max_key)
print("maximum value:",d[max_key])

# 6. Create a dictionary with 5 country - capital pairs, print all keys and values separately
countries = {
    "India" : "New Delhi",
    "Italy" : "Rome",
    "France" : "Paris",
    "Japan" : "Tokyo",
    "Australia" : "Canberra"
}
print("Countries:")
for country in countries.keys():
    print(country)

print("\nCapitals:")
for capital in countries.values():
    print(capital)

# 7. Create a dictionary of numbers (1 to 5) where values are their squares. #output {1:1,2:4.....}.
squares = { i: i**2 for i in range(1,6)}
print(squares)

# 8. Merge two dictionaries. If keys are same add  their values.
d1 = {'a': 10, 'b':20}
d2 = {'b': 5, 'c': 15}
merged ={} 
for keys,value in d1.items():
    merged[ keys ] = value

for keys,value in d2.items():
    merged[keys] = merged.get(keys,0) + value

print(merged)
# 9. Invert a dictionary (key become values and value become key). 
d = {"a":2, "b":3, "c":4}
inverted = {value: key for key, value in d.items()}
print(inverted)

# 10. Create a nested dictionary for 3 students with : Name, Age, Marks
students = {
1 : {"name":"Stark","Age" : 23,"marks":89},
2 : {"name":"Thor","Age" : 21,"marks":90},
3 : {"name":"Thor","Age" : 19,"marks":95}
}

for key, value in students.items():
    print(f"{key}:{value}")
print()