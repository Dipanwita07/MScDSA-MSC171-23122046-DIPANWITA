class Student:
    def __init__(self,a,b):
        self.name = a
        self.stu_class = b
        
    def __str__(self): #str is used to return the string value
        return self.name
abc = Student("Alwin","Ds") #object should be defined under class
print(abc.name,abc.stu_class)
print(type(abc))