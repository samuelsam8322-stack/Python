# if,elif,else statement 
a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter your third number: "))
if (a>b) and (a>c):
    print(f"{a} is greater number")
elif (b>a) and (b>c):
    print(f"{b} is greater number")
else:
    print (f"{c} is greater number")