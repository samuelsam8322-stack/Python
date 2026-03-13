# 1. Given two lists, return the set of common elements that appear more than once in both lists.
list1 = [1, 2, 2, 3, 4, 4]
list2 = [2, 2, 4, 4, 5]
result = set()
for i in list1:
    if list1.count(i) > 1 and list2.count(i) > 1:
        result.add(i)
print(result)


# 2.Create a set of unique words from a sentence, where words are separated by spaces and
# punctuation marks should be ignored.

sentence = ("Hello World, Welcome to Python!.")
for p in ",.!?;:":
    sentence = sentence.replace(p, "")
words = set(sentence.split())
unique_words = set(words)
print(unique_words)


#3.Write a function that takes a list of numbers and returns the largest subset such that the 
# sum of the subset is even.
numbers = [1, 2, 3, 4, 5]
def largest_even_subset(nums):
    if sum(nums) % 2 == 0:
        return nums
    
    # if sum is odd, remove one odd number
    for n in nums:
        if n % 2 != 0:
            nums.remove(n)
            break
    
    return nums

# numbers = [1, 2, 3, 4, 5]
print(largest_even_subset(numbers))


# 4.Given a set of integers, write a function that returns a new set containing 
# subsets of the original set.
original_set = {1, 2, 3}
def all_subsets(s):
    s = list(s)  
    subsets = [[]]  # start with empty subset
    
    for elem in s:
        # add current element to all existing subsets
        subsets += [current + [elem] for current in subsets] 
    
    # convert each subset to set
    return [set(sub) for sub in subsets]

print(all_subsets(original_set))

# 5. Check if two sets are equal, considering their elements but ignoring the order 
# (i.e., set equality).

set1 = {1, 2, 3}
set2 = {3, 2, 1}

if set1 == set2:
    print("Sets are equal")
else:
    print("Sets are not equal")


# 6.Write a program that finds the intersection of multiple sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 3, 7, 8}
result = set1.intersection(set2, set3)
print("Intersection of sets:", result)

# 7.Find the set difference of multiple sets.
# define sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set3 = {4, 6}
set4 = {2, 5}
result = set1.difference(set2, set3, set4)
print("Set Difference:", result)

# 8. Given a list of sets, write a program to return the set containing elements that are present
# in every set in the list.
sets_list = [
    {1, 2, 3, 4},
    {2, 3, 5},
    {2, 3, 6, 7}
]
common_elements = set.intersection(*sets_list)
print("Common elements in all sets:", common_elements)


# 9.Write a function that checks if a set of strings forms a palindrome when concatenated together.

def check_palindrome(s):
    word = "".join(s)
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

# example
s = {"ma", "dam"}
check_palindrome(s)


# 10.Given a set, find the number of distinct subsets where the sum of the elements in each
# subset is divisible by a given integer.
def count_subsets(s, k):
    s = list(s)
    count = 0
    n = len(s)

    for i in range(1 << n):
        total = 0
        for j in range(n):
            if i & (1 << j):
                total += s[j]
        if total % k == 0:
            count += 1

    return count

s = {1, 2, 3, 4}
k = 3

print("Number of subsets:", count_subsets(s, k))

# 11.Write a program that finds the longest consecutive sequence in an unsorted list of 
# numbers using sets.

def longest_consecutive(nums):
    s = set(nums)
    longest = 0

    for n in s:
        if n - 1 not in s:  
            length = 1
            while n + length in s:
                length += 1
            longest = max(longest, length)

    return longest

nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))

# 12.Given two sets, find the symmetric difference, but only include elements that appear 
# more than once across both sets.
from collections import Counter

a = [1, 2, 2, 3, 4]
b = [3, 4, 4, 5, 6]

count = Counter(a + b)

result = []

for x in set(a) ^ set(b):   # symmetric difference
    if count[x] > 1:        # appears more than once
        result.append(x)

print(result)

# 13. Write a function that checks if there exists a pair of numbers in a set that
#  sum to a specific target.
def has_pair_with_sum(nums, target):
    seen = set()

    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)

    return False

numbers = {1, 4, 5, 7, 9}
target = 10

print(has_pair_with_sum(numbers, target))

# 14.Write a function to determine whether a set is a proper subset of another set.
def is_proper_subset(a, b):
    return a < b

A = {1, 2}
B = {1, 2, 3, 4}

print(is_proper_subset(A, B))

# 15.Write a function that returns the elements in a set which are not present in any 
# of the other sets from a list of sets.
def unique_elements(main_set, sets_list):
    others = set()
    
    for s in sets_list:
        others = others | s   
    
    return main_set - others  

A = {1, 2, 3, 4}
sets_list = [{2, 5}, {3, 6}, {7}]

print(unique_elements(A, sets_list))

# 16.Find all possible subsets of a set and return the ones where the sum of elements is prime.
from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_sum_subsets(s):
    result = []
    s = list(s)

    for i in range(1, len(s)+1):
        for sub in combinations(s, i):
            if is_prime(sum(sub)):
                result.append(sub)

    return result

A = {1, 2, 3}
print(prime_sum_subsets(A))


# 17.Create a set of all permutations of a given list of characters.
from itertools import permutations

def permutation_set(chars):
    return set(permutations(chars))

# Example
chars = ['a', 'b', 'c']
result = permutation_set(chars)

print(result)

# 18.Check if a set contains a subset of elements that sum up to a specific value.

def has_subset_sum(s, target):
    s = list(s)
    for r in range(1, len(s)+1):
        for subset in combinations(s, r):
            if sum(subset) == target:
                return True
    return False

nums = {1, 2, 3, 4}
target = 6

print(has_subset_sum(nums, target))


# 19.Find the number of elements that appear in exactly one set from a list of sets.

def unique_count(sets_list):
    count = Counter()
    
    for s in sets_list:
        for elem in s:
            count[elem] += 1  
    
    return sum(1 for elem in count if count[elem] == 1)

sets_list = [{1,2,3}, {2,4}, {3,5}]
print(unique_count(sets_list))

# 20. Write a function that finds the union of all sets, but only includes elements that
# appear more than once across all sets

def union_multiple_occurrences(sets_list):
    count = Counter()
    
    for s in sets_list:
        for elem in s:
            count[elem] += 1 

    return {elem for elem, c in count.items() if c > 1}

sets_list = [{1, 2, 3}, {2, 3, 4}, {3, 5}]
print(union_multiple_occurrences(sets_list))


