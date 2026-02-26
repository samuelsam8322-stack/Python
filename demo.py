# a=input("Enter your name:")
# b=int(input("Enter the value of a: "))
# c=int(input("Enter the value of b: "))
# print("The sum of a and b is: ",b+c)
# d=int(input("Enter the total area of Square: "))


a = []

print('Students score:')
for i in range(3):
    score = float(input())
    a.append(score)

print("Scores:", a)

total = 0
for i in a:
    total = total + i
print("Sum:", total)

count = 0
for i in a:
    count = count + 1
print("Count:", count)

average = total / count
print(f"Average: {average:.2f}")