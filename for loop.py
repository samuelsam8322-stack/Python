#For loop
for i in range(10):
    if i%2==0:
        print(i)

#Task in for loop
# 1. To print numbers from 1 to 10
for i in range(1,10):
    print(i)
# 2.To print even numbers from 1 to 20
for i in range(1,20):
    if i%2==0:
        print(i)

# 3.To print odd numbers from 1 to 20
for i in range(1,20):
    if i%2==1:
        print(i)

# 4. To print number from 10 to 1 in reverse order
for i in range(10,0,-1):
    print(i)

#5. To print the square of each number from  1 to 10
for i in range(1,11):
    print(i**2)

#6. to print the multiples of 5 up to 50
for i in range(5,51,5):
    print(i)

# 7.To find the sum of number from 1 to 10
total = 0
for i in range(1,11):
    total += i
    print("sum: ",total)

# 8. to find the sum of even numbers from 1 to 20
total = 0
for i in range(2,21,2):
    total += i
    print("The sum of even numbers: ",total)

# 9. to find the sum of odd numbers from 1 to 20
total = 0
for i in range(1,21,2):
    total += i
    print("The sum of odd numbers: ",total)

# 10. to print multiplication table of 7
for i in range(1,11):
    print("7 x ",i,"=",7*i)

# 11. To print numbers divisible by 3 from 1 to 30
for i in range(3,31,3):
    print(i)

# 12. To find the factorial of 5 using for loop
num = 5
factorial = 1
for i in range(1,num+1):
    factorial *= i
    print("Factorial of",num,"is",factorial)

# 13. To print numbers from 1 to n (take any fixed n like 15)
for i in range(1,16):
    print(i)

# 14. To count the digits of a number (ex:54321)
num = 567890
count = 0
for digit in str(num):
    count += 1
    print("Number of digits: ",count)

# 15. a program to reverse a number (ex:1234-4321)
num = 12345
rev = 0
length = len(str(num))
for i in range(length):
    digit = num%10
    rev = rev * 10 + digit
    num //= 10
    print("Revesered number: ",rev)

# 16. to print the digits of a number
num = 987
for digit in str(num):
    print(digit)

# 17. to find the sum of digits from a number
num = 765
sum_digits = 0
for digit in str(num):
    sum_digits += int(digit)
    print("Sum of digits: ",sum_digits)

# 18. to calculate the power of a number(ex:2**5)
base = 2
exponent = 5
result = 1
for _ in range(exponent):  
    result *= base         
    print(f"{base}^{exponent} =", result)


#19. to check if a number is prime or not ,using for loop
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")

  
# 20. to print a right triangle star pattern 
rows =  5
for i in range(1,rows+1):
    print("*"*i)