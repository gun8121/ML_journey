# catch invalid input with try / except block

# value = 10/0 -  division error
# so instead we can break down 
try:
    number = int(input("Enter a number: "))
    print(number)
# instead of jst an except
# we can break it down into zerodivisionerror and valueerror
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("Invalid Input")
