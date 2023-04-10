# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# itertools modules is a collection of tools for handling iterators
# data types that can be used in a for loop
# most common iterator is list

# product - result of two or more numbers when multiplied together
from itertools import product
a = [1,2,3]
b = [3]
prod = product(a,b)
print(list(prod))

prod = product(a,b, repeat=2)
print(list(prod))

# permutations - nPr = n! / (n-3)!
from itertools import permutations
perm = permutations(a, 2) # specify length of permuation length 2
print(list(perm))

# combinations - all possible combinations with specified length
from itertools import combinations
a = [1,2,5,3,4]
comb = combinations(a, 2)
print(list(comb))
# this has no repetitions

# combinations_with_replacements
from itertools import combinations_with_replacement
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# accumulate - sum of accumulated sum or any binary function
from itertools import accumulate
import operator
acc = accumulate(a, func=operator.mul)
print(list(acc))
acc = accumulate(a, func=max)
print(list(acc))

# groupby - iterator that returns keys and groups from an iterable
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

# lamda - small one line function

a = [1,2,3,4]
group_obj = groupby(a, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))

# another example

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
          {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28},]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

# infinite iterators - count, cycle, repeat
from itertools import count, cycle, repeat
# infinite loop starting from 10
for i in count(10):
    print(i)
    if i == 15:
        break

# cycle through 1,2,3 inifinitely
a =[1,2,3]
for i in cycle(a):
    print(i)

# repeat
a =[1,2,3]
for i in repeat(1, 4): # second argument how many times to repeat
    print(i)

