# Create an empty list to store the tickets
tickets = []

# Define a function to add a new ticket
def train_add_ticket():
    totalCounter = 0
    total_train_collection = 0
    # Get the required details from the user
    TrainNo = input("Enter Train No: ")
    DateOfJourney = input("Enter date of journey: ")
    From = input("Enter the place from where the journey will start: ")
    to = input("Enter the place till where you want to travel: ")
    baseFair = float(input("Enter the fare: "))
    totalPassenger = int(input("Enter the total no. of passengers: "))
    for i in range(totalPassenger):
        PassengerName = input("Enter the name: ")
        age = int(input("Enter the Age: "))
        sex = input("Enter the gender: ")
        berth = input("Enter the berth preference: ")

        # Create a dictionary to store the passenger details
        passenger = {
            "Passenger Name": PassengerName,
            "Age": age,
            "Sex": sex,
            "Berth ": berth,
        }

        # Add the passenger details to the list
        tickets.append(passenger)
        totalCounter = totalCounter + totalPassenger
    totalFair = float(baseFair*totalPassenger)
    ticket = {"Train No" : TrainNo, 
              "Date of Journey" : DateOfJourney, 
              "From" : From, 
              "To" : to,
              "Base Fair": baseFair,
              "No of passenger": totalPassenger,
              "Total fair": totalFair}

    # Add the ticket details to the list of tickets
    tickets.append(ticket)

    # Print the ticket details
    print("Ticket added successfully!")
    print(ticket)
    print(tickets)
    print(totalCounter,totalFair)
total_tickets = len(tickets)
print("Total tickets:", total_tickets)
print("Total fare collected:", total_train_collection)
