tickets=[] #empty list
totalCounter = 0
total_train_collection = 0

def train_add_ticket(): #define the function
    import random
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
    From=input("enter the place from where the journey will start: ")
    to=input("enter the place till where you want to travel: ")
    baseFair=float(input("enter the fare: "))
    totalPassenger=int(input("enter the total no. of passengers"))
    for i in range(totalPassenger):
        PassengerName=input("enter the name: ")
        age=int(input("enter the Age: "))
        sex=input("enter the gender: ")
        berth=input("enter the berth preference: ")
        passenger={"Passenger name":PassengerName,"AGE":age,"Sex":sex,"Berth":berth}
        tickets.append(passenger)
        totalCounter = totalCounter + 1
    totalFair=float(baseFair*totalPassenger)
    ticket = { "Train No": TrainNo,
                 "PNR NO":f,
                 "Date of Journey": DateOfJourney,
                 "From": From,
                 "To": to,
                 "Base Fair": baseFair,
                 "No of passenger": totalPassenger,
                 "Total fair": totalFair } #dict
    total_train_collection = total_train_collection + totalFair
    tickets.append(ticket)
    print("Ticket added successfully!")
    
    Btickets = []  # empty list
# totalCounter = 0
total_bus_collection = 0

def bus_add_ticket():  # define the function
    global totalCounter  # Declare totalCounter as a global variable
    global total_bus_collection
    BusNo = input("Enter Bus No: ")
    DateOfJourney = input("Enter date of journey: ")
    From = input("Enter the place from where the journey will start: ")
    to = input("Enter the place till where you want to travel: ")
    baseFare = float(input("Enter the fare: "))
    totalPassenger = int(input("Enter the total number of passengers: "))
    
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
    
    totalFare = float(baseFare * totalPassenger)
    
    ticket = {
        "Bus No": BusNo,
        "Date of Journey": DateOfJourney,
        "From": From,
        "To": to,
        "Base Fare": baseFare,
        "No of Passengers": totalPassenger,
        "Total Fare": totalFare
    }  # dictionary
    
    total_bus_collection = total_bus_collection + totalFare
    Btickets.append(ticket)
    print("Ticket added successfully!")
Ftickets = []  # empty list
# totalCounter = 0
total_flight_collection = 0

    
def flight_add_ticket():
    global totalCounter  # Declare totalCounter as a global variable
    global total_flight_collection

    Airline = input("Enter Airline: ")
    FlightNo = input("Enter Flight No: ")
    DateOfJourney = input("Enter date of journey: ")
    DepartureAirport = input("Enter departure airport: ")
    ArrivalAirport = input("Enter arrival airport: ")
    DepartureTime = input("Enter departure time: ")
    ArrivalTime = input("Enter arrival time: ")
    baseFare = float(input("enter the fare: "))
    totalPassenger = int(input("enter the total no. of passengers"))

    for i in range(totalPassenger):
        PassengerName = input("enter the name: ")
        age = int(input("enter the Age: "))
        sex = input("enter the gender: ")
        seat = input("enter the seat preference: ")
        passenger = {"Passenger name": PassengerName, "AGE": age, "Sex": sex, "Seat": seat}
        Ftickets.append(passenger)
        totalCounter = totalCounter + 1

    totalFare = float(baseFare * totalPassenger)

    ticket = {
        "Airline": Airline,
        "Flight No": FlightNo,
        "Date of Journey": DateOfJourney,
        "Departure Airport": DepartureAirport,
        "Arrival Airport": ArrivalAirport,
        "Departure Time": DepartureTime,
        "Arrival Time": ArrivalTime,
        "Base Fare": baseFare,
        "No of Passengers": totalPassenger,
        "Total Fare": totalFare
    }  # dictionary

    total_flight_collection = total_flight_collection + totalFare
    Ftickets.append(ticket)
    print("Ticket added successfully!")



def view_tickets():
    print("train", tickets)
    print("bus", Btickets)
    print("flight", Ftickets)
    print("total bus", total_bus_collection)
    print("total train", total_train_collection)
    print("total flight", total_flight_collection)
    print("total ticket sale", totalCounter)
    print("total sales", (total_bus_collection + total_train_collection + total_flight_collection))

    
   # Main loop
while True:
    print("Ticket Management System")
    print("1. Add Train Ticket")
    print("2. Bus Tickets")
    print("3. Flight Tickets")
    print("4. View Ticket")
    print("5. Quit")
    print("*"*30)

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        train_add_ticket()
    elif choice == "2":
        bus_add_ticket()
    elif choice == "3":
        flight_add_ticket()
    elif choice == "4":
        view_tickets()
    elif choice == "5":
        print("Good Bye")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
