#define an empty list to store tickets

tickets =  []

#Function to add a new ticket

def add_ticket():
     TrainNo = input("Enter train no:")
     DateOfJourney = input("Enter date of journey: ")
     From= input("Enter the place from where the journey will start: ")
     To= input("enter the place till where you want to travel: ")
     baseFair=float(input("enter the fair: "))
     totalPassenger= int(input("enter the total no of passenger"))
     totalFair = float(baseFair*totalPassenger) 
     ticket = {"Train No" : TrainNo,"Date of journey" : DateOfJourney, "From" : From, "To": To,"Base Fair" : baseFair, "No of passenger" : totalPassenger,"Total fair" : totalFair}
     tickets.append(ticket)
     print("Ticket added successfully!")

#Function to view all tickets

def view_tickets():
     print("Here are all the tickets:")
     for ticket in tickets:
         print(ticket)

#Function to search for a ticket

def search_ticket(TrainNo):
     found = False
     for ticket in tickets:
         if ticket["Train No"] == TrainNo:
             found = True
             print("Ticket found:")
             print(ticket)
             break
     if not found:
         print("Ticket not found!")

#Function to delete a ticket

def delete_ticket(TrainNo):
     found = False
     index = 0
     for ticket in tickets:
         if ticket["Train No"] == TrainNo:
             found = True
             break
         index += 1
     if found:
         tickets.pop(index)
         print("Ticket deleted successfully!")
     else:
         print("Ticket not found!")

#Main function

def main():
     while True:
         print("Select an option:")
         print("1. Add ticket")
         print("2. View tickets")
         print("3. Search ticket")
         print("4. Delete ticket")
         print("5. Exit")
         option = int(input("Enter your option: "))

         if option == 1:
             add_ticket()
         elif option == 2:
             view_tickets()
         elif option == 3:
             TrainNo = input("Enter the train number of the ticket you want to search: ")
             search_ticket(TrainNo)
         elif option == 4:
             TrainNo = input("Enter the train number of the ticket you want to delete: ")
             delete_ticket(TrainNo)
         elif option == 5:
             break
         else:
             print("Invalid option!")

if __name__ == "__main__":
    main()
