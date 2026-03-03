# pattern programs
# 1. Star square pattern
row = 5
for i in range(row):
    for j in range(row):
        print("*",end=" ")
    print()

# 2. Right Triangle Star pattern
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()

# 3. Inverted Right triangle pattern 
n = 5
for i in range(n , 0, -1):
    for j in range(i):
        print("*",end=" ")
    print()
    
# 4.  Half Pyramid pattern
n = 4 
for i in range(1,n+1):
    print(" "*(n - i),end= "")
    for j in range(i):
        print("* ",end = "")
    print()

# 5. Number Triangle pattern 
n = 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()

# 6. Floyd's pattern
n = 4
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num,end = "")
        num += 1
    print()


# 7. Diamond pattern 
n = 5

# Upper part
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)