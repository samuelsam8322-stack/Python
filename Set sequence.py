# Set : * Unordered collection of unique items
#       * Does'nt allow duplicates
#       * Unindexed
#       * Mutable(change)

mySet = {10,20,30,40}
print(type(mySet))
print(mySet)

# Add:
mySet.add(50)
print(mySet)

# Update: add multiple elements(from any iterable)
myTuple = ('aaa','bbb','ccc')
mySet.update(myTuple)
print(mySet)

# Remove: remove element. if the element is not found, show key error.
mySet.remove(40)
print(mySet,"after remove")

# Discard: remove element. doesn't show any error , if the element is not present.
mySet.discard(90)
print(mySet,"After discard")

# pop : remove random element.
mySet.pop()
print(mySet,"asddf")

# clear : clear the set
mySet.clear()
print(mySet)

# Union : returns all elements, from both sets( OR symbol | ).
set1 = {1,2,3,4}
set2 = {2,4,5,6}
print(set1.union(set2))

# Intersection: returns the common element, fromm the both sets ( AND symbol & ).
print(set1.intersection(set2))

# Differenece : elements in the first set but not in the second( NOT symbol - ).
print(set1.difference(set2))

# Symmetric_difference :elements in either sets but not both( XOR symbol ^ ).
print(set1.symmetric_difference(set2))


# Relationship test methods : returns Boolean 

# issubset(): checks subset (same element only)
print({1,2,3}.issubset({1,2,3,4}))

# issuperset():same elements and also multiple values.
print({10,20,30,40}.issuperset({20,30,40,78}))

# isdisjoint():
print({'a','b','c'}.isdisjoint({'d','e','f','g'}))