# Sets: unordered, mutable, no duplicates
# unlike lists or tuples it does not allow for duplicates

# curly bracket same like dictionary, but we don't assign a key
myset = {1,2,3}
print(myset)
print(type(myset))

# duplicates but wont be returned
myset = {1,2,3,1,2}
print(myset)

# to find how many different values we have in list
myset = set("Hello")
print(myset)

# to get blank set
myset = {}
print(type(myset)) # type = dictionary

myset = set()
print(type(myset)) # type = set

# add elements to empty set
myset.add(1)
myset.add(2)
myset.add(3)

print(myset)

# remove elements

myset.remove(3)
print(myset)
# if element is not present then throws key error

myset.discard(2)
print(myset)
# if element is not present does not throw any error

myset.clear() # empty set

myset.add(1)
myset.add(2)
myset.add(3)

print(myset)

myset.pop() # removes arbitrary set

# iterate
for i in myset:
    print(myset)

# check if element is in set
if 2 in myset:
    print("yes")

# union & intersection
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

# union combines two without duplicates
u = odds.union(evens)
print(u)

# intersection of two sets - only takes elements found in both sets
# 겹치는 것  찾ㅣ
i = odds.intersection(primes)
print(i)

# difference of two sets
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
# return all sets from the first that are not in the second set
# A에서 안겹치는 것  찾기
diff = setA.difference(setB)
print(diff)

# symmetric_difference
# 둘다 에서 안겹치는 것 찾음
symm = setA.symmetric_difference(setB)
print(symm)

# modify sets in place (ofcourse without duplication)
setA.update(setB)
print(setA)

# intersection update method
# only updates with sets found in both
setA.intersection_update(setB)
print(setA)

# difference update method
# updates the set by removing the sets found in other set
setA.difference_update(setB)
print(setA)

# symmetric_difference_update
# same thing but updates it

# supset superset
setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {7,8}
# subset
print(setA.issubset(setB)) # false
# this checks if all sets of setA is in setB
print(setB.issubset(setA)) # true

# superset opposite of subset
# true if all elements of second set is in first set
print(setA.issuperset(setB)) # true
print(setB.issuperset(setA)) # false

# isdisjoint
# true if both sets have no intersection
print(setA.isdisjoint(setB)) # false
print(setA.isdisjoint(setC)) # true

# copying method
setD = set(setA)
setD = setA.copy()

# frozen set
# immutable set data type
a = frozenset([1,2,3,4])
print(a)
print(type(a))