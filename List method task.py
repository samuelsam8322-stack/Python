# 1. write a python program to print all the elements of the list using loop
myList = [5,10,15,20,30]
for i in myList:
    print(i)

# 2. write a python program to print only the even numbers from a list.
numbers = [4,87,30,24,63,2]
for i in numbers:
    if i % 2 == 0:
        print(i)

# 3. write a python program to print only the odd numbers from a list.
numbers = [4,87,30,24,63,2]
for i in numbers:
    if i % 2 == 1:
        print(i)

# 4. write a python program to find the sum of all numbers from a list.
numbers = [8,12,15]
total = 0
for i in numbers:
    total+=int(i)
print("sum = ",total)

# 5. write a python program to find largest number from a list using a loop.
numbers = [23,56,33,98,19]
largest = 0
for i in numbers:
    if i > largest:
        largest = i
print(largest)

# 6. write a python program to find the smallest number from a list using a loop.
numbers = [12,34,56,78,11]
smallest = 0
for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)

# 7. write a python program to count how many positive numbers are in a list.
numbers =[12,-34,46,-56,97,-2]
count = 0
for i in numbers:
    if i >= 0:
        count += 1
print(count)


# 8. write a python program to count how many negative numbers are in a list.
numbers =[12,-34,46,-56,97,-2]
count = 0
for i in numbers:
    if i < 0:
        count += 1
print(count)

# 9. Write a python programm to reverse a list without using the .reverse()method
myList = [10,20,35,60,98]
print(myList[::-1])

# 10. write a python program to count how many odd and even numbers are present in a list.
mylist = [23,34,45,57,98,24]
even_count = 0
odd_count = 0
for i in mylist:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers: ",even_count)
print("Odd numbers : ",odd_count)

# 11. write a python program to find and print the index of a specific value in a list.
myList = [78,43,90,76,26,18]
print(myList.index(26))

# 12. write a python program to replace all negative numbers in a list with 0.
myList=[23,-34,22,-89,-45]
for i in range(len(myList)):
    if myList[i]< 0:
        myList[i] = 0
print(myList)

# 13. write a python program to print all numbers greater than 50 from a list.
myList = [78,45,56,90,13,52,28,39,83]
for i in myList:
    if i > 50:
        print(i)

# 14. write a python program to create a new list containing the squares of a each element.
myList = [10,12,14,16,18,20]
newList = []
for i in myList:
    newList.append(i**2)
print(newList)


# 15. write a python program to print all the duplicate values in a list.
myList = [3,8,9,3,6,9,8,5,10]
duplicates =[]
for i in myList:
    if myList.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)

# 16. write a python program to print list elements until the number 50 appears (stop when found).
myList = [5,15,20,35,45,50,60,70]
for i in myList:
    if i == 50:
        break
    print (i)

# 17. write a python program to count how many numbers in a list are divisible by 5.
myList = [ 5,15,23,59,50,75,98]
count = 0 
for i in myList:
    if i % 5 == 0:
        count += 1
print(count)

# 18. write a python program to find the second largest number in a list using loop statement.
numbers =[20,30,40,25,33,46]
largest = 0
sec_largest = 0
# largest number
for i in numbers:
    if i > largest:
        largest = i

# second largest
for i in numbers:
    if i > sec_largest and i != largest:
        sec_largest = i
print("Second largest numberis : ",sec_largest)


# 19. write a python program to check whether a list is sorted in ascending order.
myList = [10,23,45,34,21]
is_sorted = True
for i in range(len(myList)-1):
    if myList[i] > numbers[i +1]:
        is_sorted = False
        break
if is_sorted:
    print("List is sorted in ascending order")
else:
    print("List is Not sorted in ascending order")


# 20. write a python program to find the sum of only the even number in a list.
myList = [4,5,7,8,24,51]
total = 0
for i in myList:
    if i % 2 == 0:
        total += i
print("sum = ",total)

