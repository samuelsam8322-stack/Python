# Conditional statement
age=15
if age>=18:
    print("your are eligible to vote")
else:
    print("your are not eligible to vote")

#task

number=5
if number>=0:
    print("positive")
else:
    print("negative")

number= -14
if number>=0: 
    print("postive")
else:
    print("negative")

#task
#1.Check odd or even
a=10
if a%2==0:
    print("the value is even")
else:
    print("The value is odd")
b=9
if b%2==0:
    print("the value is even")
else:
    print("The value is odd")

#2. positive or negative
c=5
d=-5
if c>=0:
    print("positive")
else:
    print("negative")

    
if d>0:
    print("positive")
else:
    print("negative")

#3.Eligible to Vote
age=18
if age<=18:
    print("Your are eligible to Vote")
else:
    print("Ypur are not eligible to Vote")

#4.Greater of two numbers
e=20
f=30
if e>f:
    print("e is greater")
else:
    print("f is greater")

#5. Divisible by 5
g=int(input("Enter the Number: "))
if g%5==0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

#6.check pass or fail
score = 60
passmark = 45
if score >= passmark:
    print("Your are PASS")
else:
    print("Your are FAIL")

#7.The number is Two digit
num=int(input("Enter the number:"))
if 10<=num<=99:
    print("The number is Two digit")
else:
    print("The number is Not Two digit")

#8.Divisible by 10
num = int(input("Enter the Number: "))
if num%10==0:
    print("The number is divisible by 10")
else:
    print("The number is not divisible by 10")
    
#9.number greater than 100
num=150
if num>100:
    print ("The number is greater than 100")
else:
    print ("The number is not greater than 100")

#10.Vowels And Consonants
ch = input("Enter a Character: ")
if ch in "a,e,i,o,u":
    print("Vowels")
else:
    print("consonants")

#11.Number Divisible by 2 and 3
number= int(input("Enter the Number: "))
if(number%2==0 and number%3==0):
    print("The number is divisible by 2 and 3")
else:
    print("The number is not divisible by 2 and 3")

#12.Check number is zero or non-zero
num=int(input("Enter a number: "))
if num==0:
    print("The number is zero")
else:
    print("The number is non-zero")

#13.Number less than 5
num=int(input("Enter a value: "))
if num<5:
    print("The number is less than 5")
else:
    print("The number is not less than 5")
    
