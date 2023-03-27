# making a list (str, int, boolean)
friends = ["Bernard", "Jan", "Sona", "Toby", "Tony"]
#              0        1       2      3        4
#             -5       -4      -3       -2      -1
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:3])

# replacing
print(friends)
friends[1] = "Mike"
print(friends[1])
print(friends)

# using function with lists

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Bernard", "Jan", "Sona", "Toby", "Tony"]
# friends.extend(lucky_numbers)
# print(friends) = ["Bernard", "Jan", "Sona", "Toby", "Tony", 4, 8, 15, 16, 23, 42]

# adds element to the end of the list
friends.append("Creed")
print(friends)

# insert into list using index
friends.insert(1, "Alpha")
print(friends)

# remove
friends.remove("Jan")
print(friends)

# remove all elements
# friends.clear()
print(friends)

# pop - remove last item
friends.pop()
print(friends)

# finding element is in list
print(friends.index("Toby"))
# friends.index("Karen") - ValueError: 'Karen' is not in list

# count
print(friends.count("Toby"))

# sort
friends.sort()
print(friends)

# reverse
friends.reverse()
print(friends)

# copy
friends2 = friends.copy()
print(friends2)