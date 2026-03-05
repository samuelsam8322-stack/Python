# Tuples:
#        It is used to store multiple values in single variable.
#        paranthesis (), is the symbol to denote tuple (,)
 
# characteristics:
#           * 0rdered, allow duplicates, access through index and range
#           * immutable - you cannot add, remove, or change items after the tuple is created.
# Methods :
#          * count()
#          * index()

myTuple = (10,20,30,20)
print(type(myTuple))
print(myTuple)

myData = (500,)
print(type(myData))

# Index []:
print(myTuple.index(20))


# Count():
print(myTuple.count(20))


# concatenated :
concatenatedData = myTuple + myData
print(concatenatedData,"concat")

# Repeation :
myName = ("Sam")*3
print(myName)

# Unpacking :
name,age,city = ("sam",24,"LosAngles")
print("Name: ",name)
print("Age :",age)
print("City:",city)

# constructor :
depart = tuple(("CSE","EEE"))
print(depart)


# Tuple to List:
alpha = (12,13,15)
tupleToList = list(alpha)
print(tupleToList)

tupleToList.append(14)  # add value in list using append
tupleToList.append(14)
print(tupleToList)
# List to tuple:
listToTuple = tuple(tupleToList)
print(listToTuple)
print(type(listToTuple))