"""In python Pass,Break and Continue are loop control statements used to alter the flow of a 
longer loop's execution based on specific conditions.
# 1. pass - Act as a place holder that does nothing.
# 2. break - Exits the loop entirely.
# 3. continue - Skips the current iteration and moves to the next one."""

# example:

i = 1
count = 10
while i<=10:
    if i%2==0:
        print(i)
    i+=1

i = 1
count = 20
while i<=count:
    if i%2==0:
        print(i)
    i+=1

# for loop task - break
for i in range(5):
    print(i)
    if i==2:
        break

# for loop task - continue 
num = input("Enter a number:")
for i in range (10):
    if i==2:
        continue
    print(i)
    
# for loop task - break
num = 1
for i in range(6):
    if i == 4:
        break
    print(i)

