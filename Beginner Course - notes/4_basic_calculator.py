# get two numbers from user

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result) # 1 + 4 = 14??

# when input gets from user python by default converts into string
num3 = input("Enter a number: ")
num4 = input("Enter another number: ")
result_integer = int(num3) + int(num4)
print(result_integer)

# problem with calculator - decimal numbers = error
num5 = input("Enter a number: ")
num6 = input("Enter another number: ")
result_floaty = float(num5) + float(num6)
print(result_floaty)