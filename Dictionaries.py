# dictionary data types: dict{} constructor
# Ordered, mutuable, Doesn't allow duplicates
# key doesn't repeat,Values may repeat.
# {key:value} structured

student = {"name":"sam","age":24,"City":"London"}
print(student["name"])

# methods:

# 1. Get:
print(student.get("Phone"))
student['age'] = 21

# 2. Update:
#student.update(['Course'':BCA'])

# 3. pop:
student.pop('age')
print()

# 4.Pop item:
student.popitem()
print()

# 5. Clear:
student.clear()
  
print (student.items())   # gives keys,values.


for i in student.values():
    print()

for key,values in student.items():
    print(key,':',values)

# Nested dictionaries:

details = {
    "student_1": {"name":"Ajith","age":23,"City":"London"},
    "student_2": {"name":"Aakash","age":25,"City":"Los Vegas"}
    }
print(details["student_2"]["name"])


mydict = {
    "name":"Stark",
    "email":"tonystark17@gmail.com",
    "contact": 11224433,
    "marks":[90,96,99,98,85],
}
score = 0
for i in mydict["marks"]:
    score += i

print("Total:",score)
students = [
{"name":"Stark","marks":[78,96,93,98,88]},
{"name":"Thor","marks":[90,91,100,98,75]},
{"name":"Loki","marks":[100,96,94,98,100]},
{"name":"Strange","marks":[90,94,99,98,85]},
{"name":"Wanda","marks":[90,96,90,88,100]}]

for student in students:
    student["total"] = sum(student["marks"])

students.sort(key=lambda x: x["total"], reverse=True)

rank = 1
for student in students:
    student["rank"] = rank
    rank += 1

for student in students:
    print(student["rank"], student["name"], student["total"])

