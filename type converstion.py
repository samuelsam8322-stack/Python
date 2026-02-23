#Type Converstion
#implict or coercion
a=11
b=3.5
c=a+b
print(c)
print(type(c))
d=True
e=False
f=d+e
print(f)
print(type(f))
#explicit
a="24"
strToInt=int(a)
print(strToInt)
print(type(strToInt))
b=[1,2,3,4]
listToTuple=tuple(b)
print(listToTuple)
print(type(listToTuple))


#Task
#1.Int to Str
a=45
b=25
c=a+b
print(c)
intToStr=str(c)
print(intToStr)
print(type(intToStr))
z=900
print(type(z))
intToStr=str(z)
print(intToStr)
print(type(intToStr))

#2.Str to Int
f=("5000")
print(type(f))
strToInt=int(f)
print(strToInt)
print(type(strToInt))
h='08'
print(type(h))
strToInt=int(h)
print(strToInt)
print(type(strToInt))

#3.str to bool
g="1"
print(type(g))
strToBool=bool(g)
print(strToBool)
print(type(strToBool))
p="apple"
print(type(p))
strToBool=bool(p)
print(strToBool)
print(type(strToBool))

#4.bool to str
isActive=True
print(type(isActive))
boolToStr=str(isActive)
print(boolToStr)
print(type(boolToStr))
isLose=False
print(type(isLose))
boolToStr=str(isLose)
print(boolToStr)
print(type(boolToStr))

#5.Int to Bool
a=100
print(type(a))
intToBool=bool(a)
print(intToBool)
print(type(intToBool))
f=20
h=10
i=(f+h)
print(i)
print(type(i))
intToBool=bool(i)
print(intToBool)
print(type(intToBool))

#6.Bool to Int
r=True
print(type(r))
boolToInt=int(r)
print(boolToInt)
print(type(boolToInt))
q=False
print(type(q))
boolToInt=int(q)
print(boolToInt)
print(type(boolToInt))

#7.List to Tuple
w=[1,2,3]
print(type(w))
listToTuple=tuple(w)
print(listToTuple)
print(type(listToTuple))
e=["sam"]
print(type(e))
print(listToTuple)
print(type(listToTuple))

#8.Tuple to List
r=(2,3,4)
print(type(r))
tupleToList=list(r)
print(tupleToList)
print(type(tupleToList))
t=("aara","kavin")
print(type(t))
tupleToList=list(t)
print(tupleToList)
print(type(tupleToList))

#9.Tuple to Set
y=(7,8,9)
print(type(y))
tupleToSet=set(y)
print(tupleToSet)
print(type(tupleToSet))
u=('sam','aakash')
print(type(u))
tupleToSet=set(u)
print(tupleToSet)
print(type(tupleToSet))

#10.Set to List
i={"sam"}
print(type(i))
setToList=list(i)
print(setToList)
print(type(setToList))
o={87,94,65}
print(type(o))
setToList=list(o)
print(setToList)
print(type(setToList))

#11.List to Set
x=[5,6,4]
print(type(x))
listToSet=set(x)
print(listToSet)
print(type(listToSet))
c=["sandhiya"]
print(type(c))
listToSet=set(c)
print(listToSet)
print(type(listToSet))

#12.Set to Tuple
n={10,20,30}
print(type(n))
setToTuple=tuple(n)
print(setToTuple)
print(type(setToTuple))
m={"bala"}
print(type(m))
setToTuple=tuple(m)
print(setToTuple)
print(type(setToTuple))

