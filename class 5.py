class Student():
    #data members
    #name, email, phone,...
    #member functions
    def __init__(self):#initialize the value of the variable- init function #initialize the - self
        self.name = "Dipanwita"
        self.email ="hjh@gmail.com"
        self.phone = 9867567893
    
    def printStudent(self): #self- variable name
        print("Name : {}\nEmail : {}\nPhone :{}".format(self.name,self.email,self.phone))
        
    def __str__(self):
        pass
    
abith = Student() #storing in a variable
abith.printStudent()

print(abith.name) #print only one property