# Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

item = mylist[0]
print(item)
item = mylist[1]
print(item)
item = mylist[2]
print(item)
item = mylist[-1]
print(item)
item = mylist[-2]
print(item)
item = mylist[-3]
print(item)

# print all in list by order
for i in mylist:
    print(i)
    # i can be called anything

# check if item is in list
if "banana" in mylist:
    print("yes")
else:
    print("no")

if "cherry" in mylist:
    print("yes")
else:
    print("no")

# check how many items in list
print(len(mylist))

# append
mylist.append("lemon")
print(mylist)

# insert into a certain position
mylist.insert(1, "bluberry")
print(mylist)

# pop - remove last item
mylist.pop()
print(mylist)

# remove certain element
mylist.remove("cherry")
print(mylist)

# sort alphabetical
mylist.sort()
print(mylist)

# sorted in new list
new_list = sorted(mylist)
print(new_list)

# reverse list
mylist.reverse()
print(mylist)

# remove everything
mylist.clear()
print(mylist)

# new list with 5 zeros in it
mylist = [0] * 5
print(mylist)

mylist2.clear()
mylist2 = [1,2,3,4,5]

neww_list = mylist + mylist2
print(neww_list)

num_list = [1,2,3,4,5,6,7,8,9]
a = num_list[1:5] # start index + stop index
print(a)

a = num_list[:5] # dont specify start index - then start from beginning
print(a)
a = num_list[1:] # dont specify end index - then goes all the way to the end
print(a)

a = num_list[::1] # optional step index ~ every 1 step
print(a)
a = num_list[::2] # optional step index ~ every 2 step
print(a)
a = num_list[::-1] # optional step index ~ every 2 step
print(a)

# when using a copy or orig list becareful because changed to copy will effect orig
list_org = ["banana", "apple", "cherry"]

list_cpy = list_org
print(list_org)
list_cpy.append("blueberry")
print(list_cpy)
print(list_org)

# to solve this we need to make an actual copy
# list_cpy = list_org.copy()
# list_cpy = list(list_org)
# list_cpy = list_org[:] slicing

# list comprehension