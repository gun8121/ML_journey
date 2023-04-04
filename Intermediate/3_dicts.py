# Dictionary: Key-Value pairs, Unordered, Mutable
# Each key maps the key value pair to its value

mydict = {"name": "Max", "age": 28, "city": "New York"} # key name : value Max
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston") # can use the previous format to create new
print(mydict2)                                     # in this case key does not need ""

value = mydict["name"] # to find the value associated to the key
print(value)

value = mydict["age"] # to find the value associated to the key
print(value)

# value = mydict["lastname"] KeyError: 'lastname'

# adding new key + value
mydict["email"] = "max@xyz.com"
print(mydict)

# if adding new key that already exists it get over-written
mydict["email"] = "coolmax@xyz.com"
print(mydict)

# delete items
del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

# prior to python 3.7 removes arbitrary pair, after python 3.7 removes last pair
mydict.popitem()
print(mydict)

mydict = {"name": "Max", "age": 28, "city": "New York"} # key name : value Max
print(mydict)

# to see if key exist in dict
if "name" in mydict: # if wrong nothing gets executed
    print(mydict["name"])

# try except
try:
    print(mydict["name"])
except:
    print("Error")

# loop through dictionary
for key in mydict:
    print(key)

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

# copy dictionary - becareful
# most common way
mydict_cpy = mydict # both dictionary points to the same dictionary in memory
print(mydict_cpy)
# but when you modify the copy it will modify the orig

mydict_cpy["email"] = "max@xyz.com"
print(mydict)
print(mydict_cpy)

# to better improve this
mydict_cpy = mydict.copy()
mydict_cpy = dict(mydict)

# merge two dictionary
my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
my_dict2 = dict(name="Mary", age=27, city="Boston")

my_dict.update(my_dict2)
print(my_dict) 
# all key value pairs get over-written (email didnt but all existing keys got overwritten)

# any immutable type can be used as a key
my_dictt = {3: 9, 6: 36, 9:81}
print(my_dictt) 
# becareful beacuse when accessing the value

# using tuple as a key
mytuple = (8,7)
mytupledict = {mytuple: 15}
print(mytupledict) 

# using a list will cause type error because a list is mutable