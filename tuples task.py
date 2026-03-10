# 1. create a tuple that contains an integer,string, and a float.
myTuple = (83,'sam',46.9)
print(myTuple)

# 2. Access the second element of the tuple (5,10,15,20).
num = (5,10,15,20)
print(num[1])

# 3. Slice the tuple (1,2,3,4,5) to get the last two element.
numbers = (1,2,3,4,5)
print(numbers[3:])

# 4. concatenate the tuples(1,2) and (3,4).
num1 = (1,2)
num2 = (3,4)
concatenatedvalue = num1 + num2
print(concatenatedvalue)

# 5. Repeat the tuple (7,8) three lines.
myTuple = (7,8)*3
print(myTuple)

# 6. check if 15 is present in thee tuple (10,20,15,25).
numbers = (10,20,15,25)
if 15 in numbers:
    print("15 is present")
else:
    print("15 is not present")

# 7. Find the length of the tuple (3,6,9,12).
myTuple = (3,6,9,12)
print(len(myTuple))

# 8. find maximum and minimum values in the tuple(4,1,8,3).
values = (4,1,8,3)
max_values = values[0]
mini_values = values[0]
for i in values:
    if i > max_values:
        max_values = i
    if i <= mini_values:
        mini_values = i
print("Maximum value is: ",max_values)
print("Minimum values is: ",mini_values)

# 9. Convert the list [1,2,3,4] into the tuple.
myList = [1,2,3,4]
listToTuple = tuple(myList)
print(listToTuple)

# 10. convert the tuple(10,20,30) into a list.
myTuple = (10,20,30)
tupleToList = list(myTuple)
print(tupleToList)

# 11. Find the index of the element 30 in a tuple.(10,20,30,40).
elements = (10,20,30,40)
print(elements.index(30))


# 12. count how many times 2 appears in the tuple(2,3,2,4,2) 
numbers = (2,3,2,4,2)
print(numbers.count(2))


# 13. Unpack the tuple(100,200,300) into three seperate variable
num = (100,200,300)
value1,value2,value3 = num
print(value1)
print(value2)
print(value3)


# 14. Swap the value of two tuples(1,2) and (3,4).
tuple1 = (1,2)
tuple2 = (3,4)
tuple1,tuple2 = tuple2,tuple1
print("Tuple 1:",tuple1)
print("Tuple 2:",tuple2)


# 15. create the tuple that contains two other tuples(1,2),(3,4).
tuples = ((1,2),(3,4))
print(tuples)


# 16. Access the number 4 from the nested tuple((1,2),(3,4))
mytuples = ((1,2),(3,4))
print(mytuples[1][1])


# 17. Find the sum of all numbers in the tuple(5,10,15).
num = (5,10,15)
total = 0
for i in num:
    total += i
print("sum:",total)


# 18. Sort the element of the tuple(40,10,30,20) in the ascending order.
numbers = (40,10,30,20)
values = list(numbers)   #tupleToList
values.sort()
numbers = tuple(values)  #listToTuple
print(numbers)


# 19. Reverse the element of the tuple(1,2,3,4,5).
elements = (1,2,3,4,5)
reversed_tuple = elements[::-1]
print(reversed_tuple)


# 20. Check if all elements in the tuple(5,5,5,5) are identical.
numbers = (5,5,5,5)
if all (i == numbers[0] for i in numbers):
    print("All elements are identical")
else:
    print("Elements are NOt identicial")