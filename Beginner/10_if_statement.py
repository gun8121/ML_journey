'''
I wake up
If I'm hungry
  I eat breakfast

I leave my house
if it's cloudy
  I bring an umbrella
otherwise
  I bring sunglasses

Im at a restaurant
if I want meat
  I order a steak
otherwise if I want pasta
  I order spaghetti & meatballs
otherwise
  I order salad.
'''
is_male = True # boolean variable
is_tall = True

if is_male or is_tall: # only true when one or both true
    print("You are male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not tall or a male")


# or - only true when one or both true
# and - only true when both true
# not - the opposite / not true = false / not false = true

# comparison operators
# function with 3 parameter
# returns the highest number of the three

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 40, 5))