
def say_hi():
    print("Hello User")

# order the code runs 
# 1 top 2 say_hi function 3 bottom
print("Top")
say_hi()
print("Bottom")

# adding parameter

def user_hi(name):
    print("Hello " + name)

user_hi("Steve")