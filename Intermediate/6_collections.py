# collections: counter, namedtuple, ordereddict, defaultdict, deque
from collections import Counter
# counter - container that stores elements as dictionary keys and their counts as dictionary values
a = "aaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)) # only 1 most common element
print(my_counter.most_common(2)) # only 1 most common element - list with tuples in it
print(my_counter.most_common(1)[0][0]) # only 1 most common element - tuple 0 element 0
print(list(my_counter.elements())) # get all elements as a list

# namedtuple
from collections import namedtuple
# lightweight object type, similiar to a struct
Point = namedtuple('Point', 'x,y') # class of points with fields x and y
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# ordereddict
from collections import OrderedDict
# regular dictionary but they remember the order that the items were inserted
# since python 3.7 ordinary dictionary also has the function

ordered_dict = OrderedDict() 
# since python 3.7 we can just use
# ordered_dict = {}
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict) # OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])

# defaultdict
from collections import defaultdict
# similiar to usual dictionary container - will have default value if key is not assigned
d = defaultdict(int) # int as default type
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d)
print(d['e']) #key e does not exist but return value of interger = 0

# float default value
d = defaultdict(float) # float as default type
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d)
print(d['e']) #key e does not exist but return value of float = 0.0

# empty list
d = defaultdict(list) # list as default type
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d)
print(d['e']) #key e does not exist but return value of list = []

# deque - double ended queue
# add or remove elements from both ends
# both are implemented in a way be efficient
from collections import deque

dq = deque()
dq.append(1)
dq.append(2)
print(dq)
# add to left side
dq.appendleft(3)
print(dq)
# remove last element
dq.pop()
print(dq)
# remove from left
dq.popleft()
print(dq)
# remove all
dq.clear()
print(dq)

dq.append(1)
dq.append(2)
# add all elements at right side
dq.extend([4,5,6])
print(dq)
# add all left
dq.extendleft([7,8,9])
print(dq)
# move elements one place to the right
dq.rotate(1)
print(dq)
# move elements two place to the right
dq.rotate(2)
print(dq)
# move elements one place to the left
dq.rotate(-1)
print(dq)
# move elements two place to the left
dq.rotate(-2)
print(dq)