myList = [10,20,30,40,50,20]


print(myList)
print(myList[1])
print(myList[1:3])
print(myList[:4])
print(myList[3:])
print(myList[-1])
print(myList[::-2])
myList.append("sam")
print(myList,"append")
myList.pop(2)
print(myList,"pop")
myList.pop()
print(myList,"pop")


myTuple = ("CSE","IT")
myList.extend(myTuple)
print(myList)

myList.insert(1,"EEE")
print(myList,"insert")

myList.remove(20)
print(myList,"remove")


print(myList.index(50))

print(myList.count("IT"))
# lt is ordered, allow duplicates, changable


numbers = [12,4,63,1,0,56]
# numbers.sort()
# numbers.reverse()
print(numbers)

evenNumbers = []
oddNumbers = []
for i in numbers:
    if i % 2 == 0:
        # print(i)
        evenNumbers.append(i) 
    else:
        oddNumbers.append(i)
print(evenNumbers)
print(oddNumbers)


# myList =  list([10,20,30])

# myList  = ["ST001","aaa",9347534854,True]

