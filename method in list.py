myList = [10,15,20,25,30,45]
print(myList)
#index
print(myList[1])
print(myList[1:3]) #range
print(myList[:4])  
print(myList[::-1])  #reverse


# List methods and what it does
# 1. append - add an element to the end of the list

myList.append("sam")
print(myList)

# 2. pop - removes and returns item at index i (last item if not specified)

myList.pop(1)
print(myList)
myList.pop()
print(myList)

# 3. extend -add multiple items to the end 

myTuple = ("CSE","IT")
myList.extend(myTuple)
print(myList)

# 4. Insert - Inserts item x at position i
myList.insert(1,"EEE")
print(myList)

# 5. Remove-