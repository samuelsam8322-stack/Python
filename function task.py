# Function task:
#1.write a program to check even or odd using function.
num = 8
def even():
      if num % 2 == 0:
        return 'even'
      else:
        return 'odd'
result=even()
print(f'the number 8 is {result}')

# 2.write a program to check the number 12 is divisible by 2 and 3 using function.
n=12
def divisible():
      if n %2 %3 == 0 :
       return'12 is divisible by 2 and 3'
      else:
       return'12 is not divisible by 2 and 3'
result=divisible()
print(f'the number {result}')

# 3.write a program to find greater of two numbers a = 30 and b = 40 using function.
def greater(a,b):
     if a > b :
      return 'greater number is a'
     else:
      return 'greater number is b'
result=greater(30,40)
print(f'the {result}')

# 4.write a program to check vowel or consonant using function.
def check_char(ch):
     if ch in ('a','e','i','o','u'):
       return 'is vowel'
     else:
        return 'is consonant'
result= check_char('n')
print(f'the character {result}')

# 5.write a program using a function to check whether a given number is positive, negative, or zero.
def check_num(number):
     if number > 0 :
          return 'is positive'
     elif number < 0 :
          return 'is negative'
     else:
          return 'is zero'
result=check_num(-5)
print(f'the number {result}')

# 6.Write a program using a function to print numbers from 1 to 10 and also use for loop.
def num():
        for i in range(1,11):
             print(i)
num()

# 7.Write a function to print all even numbers from 1 to 20 using a for loop.
def check_num():
     for even in range(1,20):
          if even % 2 == 0 :
               print(even)
check_num()

# 8.Write a function to find the sum of numbers from 1 to n (n is given as input).
def check_num(n):
     total = 0
     for i in range (1,n+1):
          total = total + i
     return total
result = check_num(10)
print(result)

# 9.Write a function to print the multiplication table of a given number.
def check_num(n):
    for i in range(1, 11):
        print(i * n)
check_num(3)

# 10.Write a function to count how many vowels are present in a given string using a for loop.
def check_char(text):
     count = 0
     for ch in text:
        if ch in ('a', 'e', 'i', 'o', 'u'):
                count = count + 1
     return count
result=check_char('scarlet witch')
print(f'Total no. of vowel is {result}')