nameList = []
def storeName():   #to store names
    name = input("Enter the name :")
    name = name.strip().title()
    nameList.append(name)
    return name

def listNames():
    print("*"*30)
    print("Names in the List")
    print("*"*30)
    for name in nameList:
            print(name)
    print("*"*30)
    
def searchName(search):   #to search for a name
    search = search.strip().title()  
    found = False
    for name in nameList:
        if name == search:
            found = True
            break
    if found == True:
        print("Name exist in the list")
    else:
        print("Name does not exist..!")
print("*"*30)           
print("Name Management . Application") 
print("*"*30) 
while True:
    print("*"*30)
    print("1. Enter a name")
    print("2. List the names")
    print("3. Search for  a name")
    print("4. Exit")
    
    
    choice = input("Enter your choice")
    print("You have entered choice:", choice)
    
    if int(choice) ==1:  #add the name
        name = storeName()
        print("Name {} added succesfully!".format(name))
    elif int(choice) ==2:
        listNames()
    elif int(choice) ==3:
        name = input("Enter a name to be searched")
        searchName(name)
    elif int(choice) == 4:
        exit()
    else:
        print("Invalid option")
        
        
        