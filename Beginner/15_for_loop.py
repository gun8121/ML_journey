# for loop - loop through arrays
for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Carey", "Corey"]
for friend in friends:
    print(friend)

# for index in range(10):
#    print(index) # without printing out 10

# for index in range(3, 10):
#    print(index) # without printing out 10

for index in range(len(friends)):
    print(friends[index]) # without printing out 10

for indexx in range(5):
    if indexx == 0:
        print("first iteration")
    else:
        print("not first")