class petStore:
    def __init__(self,name,age,gender):
        self.name = name
        self.age=age
        self.gender = gender
    def printPet(self):
        print(self.name,self.age,self.gender)
    
    pet_details ={
        {
        "name":"beagle",
        "age":"2",
        "gender":"f"
    },
    {
        "name":"corgi",
        "age":"11",
        "gender":"m"
    }
    }
pets =[]
def add_pet():
        name = input("Enter a new breed")
        age = input("Enter the age")
        gender = input("Enter the gender")
        pet = petStore(name,age,gender)
        pets.append(pet)
        print("Pet added successfully") 
def searchName(search):    
    for name in pets:
        if name == search:
            print("Name exist in the list")
def listNames():
    print("Names in the List")
    for name in pets:
            print(name)
def delete_pet(name):
    for pet in pets:
        if pet.name == name:
        pets.remove(pet)
        print(f"breed {name} sold")
while True:
    print()
        


          