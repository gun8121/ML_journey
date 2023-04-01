# collection data type
# Tuple: ordered, immutable, allows duplicate elements
# or simply a read-only list / because it is immutable
# often used for objects that belong together
# tuple is made with ()

mytuple1 = ("Max", 28, "Boston") # most common way to write tuple
print(type(mytuple1))
mytuple2 = "Max", 28, "Boston" # no brackets but still tuple
print(type(mytuple2))
mytuple3 = ("Max") # single element - str
print(type(mytuple3))
mytuple4 = ("Max",) # single element add comma to make into tuple
print(type(mytuple4))

# tuple iterable
mytuple5 = tuple(["Max", 28, "Boston"]) 

# what is an iterable?
# https://python.cogsci.nl/basic/iterables/
# an iterable object (or simply an iterable) is a collection of elements that you can loop (or iterate) through one element at a time. Simply put, an iterable is a list-like (or array-like) object. There are many kinds of iterables, which differ in many ways, including whether they are ordered and mutable:

# An iterable is ordered if you can retrieve its elements in a predictable order
# An iterable is mutable if you can change which elements it contains
# Python has four built-in iterable types: list, dict, tuple, and set

# access elements inside tuple

item = mytuple5[1] # 0 is the first, -1 is the last
print(item)

# change element inside tuple
# mytuple5[0] = "Tim" TypeError: 'tuple' object does not support item assignment

# iterate over a tuple

for i in mytuple5: # variable can be called anything
    print(i)

# check if element is in tuple
if "Max" in mytuple5:
    print("Yes")
else:
    print("No")

# tuple with some letter in it
my_tuple = ("a","p","p","l","e")

# number of elements inside tuple
print(len(my_tuple)) #5

# find how many duplicates of an element is in tuple
print(my_tuple.count("p"))

# find first index of element in tuple
print(my_tuple.index('p')) # finds the index of the first occurance of the element

# convert tuple to a list - vice versa
my_list = list(my_tuple)
print(type(my_list))

my_tuple = tuple(my_list)
print(type(my_tuple))

# slicing in tuple
a = (1,2,3,4,5,6,7,8,9,19)

b = a[2:8] # start index and end index
print(b)

c = a[1::1]
print(c)

# unpacking
my_tuple_unpack = "Max", 28, "Boston"

name, age, city = my_tuple_unpack # number of element must equal the elements inside tuple
print(name)
print(age)
print(city)

# can unpack multiple elements with *
my_tuple_unpack_all = (0,1,2,3,4)

i1, *i2, i3 = my_tuple_unpack_all
print(i1)
print(i2) # this is everything inbetween
print(i3)

# when working with large data tuple can be more efficient
import sys
my_llist = [0,1,2,"hello", True]
my_ttuple = (0,1,2,"hello", True)
print(sys.getsizeof(my_llist), "bytes") # 104 bytes
print(sys.getsizeof(my_ttuple), "bytes") # 80 bytes

# more efficient to iterate over tuple than list
import timeit # to see how long code takes to run
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000)) # list - 0.03215924999676645 sec
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)) # tuple - 0.004277708008885384 sec