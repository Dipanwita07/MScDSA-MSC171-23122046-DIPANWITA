tickets=[] #empty list
totalCounter = 0
total_train_collection = 0

def train_add_ticket(): #define the function
    import random # IMPORTING THE RANDOM TO PRINT PNR RANDOMLY
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,9)
    d=random.randint(0,9)
    e=random.randint(0,9)
    f=str(a)+str(b)+str(c)+str(d)+str(e)
    
    global totalCounter  # Declare totalCounter as a global variable
    global total_train_collection
    TrainNo = input("Enter Train No: ")
    DateOfJourney = input("Enter date of journey: ")
    From=input("FROM : ")
    to=input("TO : ")
    baseFair=float(input("Enter the fare: "))
    totalPassenger=int(input("Enter the total no. of passengers : "))
    for i in range(totalPassenger): # ITERATING THE VALUE OF PASSENGER DETAILS
        PassengerName=input("Enter the name: ")
        age=int(input("Enter the Age: "))
        sex=input("Enter the gender: ")
        berth=input("Enter the berth preference: ")
        passenger={"Passenger name":PassengerName,"AGE":age,"Sex":sex,"Berth":berth}
        tickets.append(passenger)
        totalCounter = totalCounter + 1 
    totalFair=float(baseFair*totalPassenger) #TOTAL FAIR FOR THE PASSENGER
    ticket = { "Train No": TrainNo,
                 "PNR NO":f,
                 "Date of Journey": DateOfJourney,
                 "From": From,
                 "To": to,
                 "Base Fair": baseFair,
                 "No of passenger": totalPassenger,
                 "Total fair": totalFair } #DICTONARY
    total_train_collection = total_train_collection + totalFair #TOTAL COLLECTION OF TRAIN 
    tickets.append(ticket) #ADDING THE DICTONARY TO THE LIST
    print("Train Ticket added successfully!")
    
    Btickets = []  # empty list
total_bus_collection = 0

def bus_add_ticket():  #DEFINE THE FUNCTION TO ADD BUS TICKETS
    import random   # IMPORTING THE RANDOM TO PRINT PNR RANDOMLY
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,9)
    d=random.randint(0,9)
    e=random.randint(0,9)
    f=str(a)+str(b)+str(c)+str(d)+str(e)
    global total_bus_collection
    global totalCounter
    #USER INPUT THE BUS DETAILS
    BusNo = input("Enter Bus No: ")
    DateOfJourney = input("Enter date of journey: ")
    From = input("FROM :")
    to = input("TO :")
    baseFare = float(input("Enter the fare: "))
    totalPassenger = int(input("Enter the total number of passengers: "))
    #STORING THE DETAILS OF THE PASSENGER IN THE LIST
    for i in range(totalPassenger):
        PassengerName = input("Enter the name: ")
        age = int(input("Enter the Age: "))
        sex = input("Enter the gender: ")
        seat = input("Enter the seat preference: ")
        passenger = {
            "Passenger Name": PassengerName,
            "Age": age,
            "Sex": sex,
            "Seat Preference": seat
        }
        Btickets.append(passenger)
        totalCounter = totalCounter + 1
    #CALCULATING THE FARE FOR THE PASSENGER
    totalFare = float(baseFare * totalPassenger) 
    
    ticket = {
        "Bus No": BusNo,
        "PNR NO": f,
        "Date of Journey": DateOfJourney,
        "From": From,
        "To": to,
        "Base Fare": baseFare,
        "No of Passengers": totalPassenger,
        "Total Fare": totalFare
    }  # dictionary
    
    total_bus_collection = total_bus_collection + totalFare
    Btickets.append(ticket)   #TO STORE THE DICTONARY TO THE LIST 
    print("Bus Ticket added successfully!")
    
    Atickets = []  # EMPTY LIST
total_air_collection = 0

#FUNCTION TO ADD FLIGHT DETAILS
def air_add_ticket():  
    import random
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,9)
    d=random.randint(0,9)
    e=random.randint(0,9)
    f=str(a)+str(b)+str(c)+str(d)+str(e)
    global total_air_collection
    #ENTERING THE FLIGHT DETAILS
    FlightNo = input("Enter Flight No: ")
    DateOfJourney = input("Enter date of journey: ")
    From = input("Enter the departure airport: ")
    To = input("Enter the destination airport: ")
    baseFare = float(input("Enter the fare: "))
    totalPassenger = int(input("Enter the total number of passengers: "))
    
    #ENTERING THE PASSENGER DETAILS AND STORING IT IN THE LIDT
    for i in range(totalPassenger):
        PassengerName = input("Enter the passenger's name: ")
        age = int(input("Enter the passenger's age: "))
        sex = input("Enter the passenger's gender: ")
        seat = input("Enter the seat preference: ")
        passenger = {
            "Passenger Name": PassengerName,
            "Age": age,
            "Sex": sex,
            "Seat Preference": seat
        }
        Atickets.append(passenger)
    
    totalFare = float(baseFare * totalPassenger)
    
    ticket = {"Flight No": FlightNo,
        "PNR NO": f,
        "Date of Journey": DateOfJourney,
        "Departure Airport": From,
        "Destination Airport": To,
        "Base Fare": baseFare,
        "No of Passengers": totalPassenger,
        "Total Fare": totalFare
    }  # dictionary
    #CALCULATING THE TOTAL AIR TICKET COLLECTION
    total_air_collection = total_air_collection + totalFare
    Atickets.append(ticket)
    print("Air Ticket added successfully!")
def view_tickets():  #FUNCTION TO VIEW THE TICKET
    print("Train Tickets: ",tickets)
    print("Bus Tickets : ",Btickets)
    print("Air Tickets : ",Atickets)
    
    #FUNCTION TO VIEW THE TOTAL COLLECTION
def totalCollection():
    print("total bus collection",total_bus_collection)
    print("total air tickets collection ",total_air_collection)
    print("total train collection",total_train_collection)
    print("total ticket sales",totalCounter)
    print("total collection of all the tickets booked",(total_bus_collection + total_train_collection + total_air_collection))
    
    # Main DRIVEN PROGRAM TO ASK THE FOLLOWING FROM THE USER 
while True:
    print("Ticket Management System")
    print("1. Add Train Ticket")
    print("2. ADD Bus Tickets")
    print("3  ADD Air Ticket")
    print("4. View Ticket")
    print("5. Collection Details")
    print("6. Quit")
    print("*"*30)
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == "1":
        train_add_ticket()
    elif choice == "2":
        bus_add_ticket()
    elif choice == "3":
        air_add_ticket()
    elif choice == "4":
        view_tickets()
    elif choice== "5":
        totalCollection()
    elif choice== "6":
        print("Thanks!!!!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, 5 or 6.")

