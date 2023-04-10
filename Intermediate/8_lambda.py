# lambda arguments: express
add10 = lambda x: x + 10
print(add10(2))

def add10_func(x):
    return x + 10
print(add10_func(2))

# multiple arguments
mult = lambda x,y: x * y
print(mult(2,2))

# typically used when you need a simple function once in your code
# used as arguments that hire other functions
# sorted, map, filter, reduce

# sorted
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)

print(points2D)
print(points2D_sorted)
# sorted by the x argument

points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D)
print(points2D_sorted)

# sort according to the sum of each tuple
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])

print(points2D)
print(points2D_sorted)

# map - transforms each element with map function
# map(func, seq)

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

# list comprehension syntax
c = [x*2 for x in a]
print(c)

# filter(func, seq) func returns true or false - filter only returns all that is true
a = [1,2,3,4,5]
b = filter(lambda x: x%2==0, a)
print(list(b))

# list comprehension syntax
c = [x for x in a if x%2==0]
print(c)

# reduce(func, seq) - repeatedly applys the func to the element and returns a single value
from functools import reduce
a = [1,2,3,4,5,6]
# compute product of all the element
prod_a = reduce(lambda x,y: x*y, a) # reduce func should always have two variables
print(prod_a)