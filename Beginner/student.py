# create our own data type
# class - define your own data type
# program representing a student
# modeling a student data type

class Student: 
    def __init__(self, name, major, gpa, is_on_probation): 
        # initialize function can map out what attributes it should have
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation