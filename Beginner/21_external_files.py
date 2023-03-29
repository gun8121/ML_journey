# reading from external files

# r stands for read only / w stands for write editable / 
# a append add new information / r+ reading plus write
employee_file = open('21_external_file.txt', "r")

# print(employee_file.readlines()) 
# .readable() - boolean to show if readable
# .read() - reads the whole file
# .readline() - reads first line then moves cursor to next line
# .readline() - reads second line then moves cursor to next line
# .readlines() - takes all the lines and puts it into an array
for employee in employee_file.readlines():
    print(employee)

employee_file.close() # need to close file 


