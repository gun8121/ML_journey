# create our own data type
# class - define your own data type
# program representing a student
# modeling a student data type

class Student: 
    def __init__(self, name, major, gpa): 
        # initialize function can map out what attributes it should have
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        