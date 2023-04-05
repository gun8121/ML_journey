# String: ordered, immutable, text representation
# single or doulbe quotes
my_string = "Hello World"
print(my_string)

my_string = 'Hello World'
print(my_string)

# becareful when you have multiple quotes inside
my_string = 'I\'m a programmer'
print(my_string)
my_string = "I'm a programer"
print(my_string)
my_string = '''Hello
world''' # multiline
print(my_string)
my_string = '''Hello \
world''' # singleline
print(my_string)

# access characters or substring
my_string = "Hello World"
char = my_string[0] # positive starts at 0 / negative starts at -1
print(char)

# we cannot change a character
# my_string[0] = 'h' because strings are immutable

substring = my_string[1:5] # starts at index 1 up to 5 but 5 is excluded
print(substring)

substring = my_string[:5] # starts from beginning up to 5 but 5 is excluded
print(substring)

substring = my_string[1:] # starts at index 1 up to the end
print(substring)

substring = my_string[::2] # gets char every 2 steps
print(substring)

# concatenated string
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

# iterate over string with for in loop
for i in greeting:
    print(i)

# check if character is inside string
if 'e' in greeting:
    print('yes')
else:
    print('no')

# check if substring is inside string
if 'ello' in greeting:
    print('yes')
else:
    print('no')

# blank space
my_string = '    Hello World     '
print(my_string)
my_string = my_string.strip()
print(my_string)

# uppercase
print(my_string.upper())

# lowercase
print(my_string.lower())

# check if string starts with
print(my_string.startswith('Hello')) # true
print(my_string.startswith('World')) # false

# check if string ends with
print(my_string.endswith('Hello')) # false
print(my_string.endswith('World')) # true

# find the index of first instance of the character in string
print(my_string.find('o')) # 4
# also check for substring
print(my_string.find('lo')) # 3
# count the number of char or substring
print(my_string.count('o'))
# replace character or substring inside string
print(my_string.replace('World', 'Universe')) 
# if there is a typo with the word to replace it returns the original


my_string = 'how are you doing'
my_list = my_string.split() # by default the argument is space / so splits string by each space
print(my_list)

my_string = 'how,are,you,doing'
my_list = my_string.split(',') # by default the argument is space / so splits string by each space
print(my_list)

# convert list into string
new_string = ' '.join(my_list)
print(new_string)

my_list = ['a'] * 6
print(my_list)

from timeit import default_timer as timer

# bad python code because string is immutable
# this operation is expensive because
# 1. it creates a new string
# 2. then adds i to the string
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop-start)
# 2.0839943317696452e-06

# better to use the join function
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop-start)
# 5.830079317092896e-07

# formatting a string
# %, .format(), f-String

# %s = string
var = "Tom"
my_string = "the variable is %s" % var # %s placeholder - % var fill the placeholder with var
print(my_string)

# %d - d = integer decimal value
var = 3
my_string = "the variable is %d" % var # %s placeholder - % var fill the placeholder with var
print(my_string)

# %f - floating point value (by default 6 digits after decimal point)
var = 3.12652
my_string = "the variable is %f" % var # %s placeholder - % var fill the placeholder with var
print(my_string)

var = 3.12652 # .2f (2 digits after decimal point)
my_string = "the variable is %.2f" % var # %s placeholder - % var fill the placeholder with var
print(my_string)

var = 3.12652
my_string = "the variable is {}".format(var) # {} is the placeholder / new way
print(my_string)

var = 3.12652
my_string = "the variable is {:.2f}".format(var) # {} is the placeholder / new way
print(my_string)

var = 3.12652
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2) # {} is the placeholder / new way
print(my_string)

# new way is to use the f string (since python 3.6) 
# f-String recommended and is also faster
var = 3.12652
var2 = 6
my_string = f"the variable is {var} and {var2}" # {} is the placeholder / new way
print(my_string)

# add mathematical operation to be evaluated at run time
my_string = f"the variable is {var*2} and {var2}" # {} is the placeholder / new way
print(my_string)