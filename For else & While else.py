# For else :
#  for else is executed after the for loop completed its iteration over the entire sequence,
#  but only if a break statement didn't terminate the loop.

items = ["aaa","bbb","ccc"]
search_items = "ddd"
for i in items:
    if i == search_items:
        print(f"{search_items} id found")
else:
    print(f"{search_items} is Not found")


# While else:
# In Python, a while loop  is executed when the loop terminates normally, meaning its condition becomes
# False. The else block is not executed if the loop is terminated  prematurely by a break statement, 
# a return statement, or an exception. 


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
