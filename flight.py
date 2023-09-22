
flights = {
    "DTK253": {
        "airline": "Indigo",
        "departure_airport": "Netaji Subhas Chandra Bose International Airport",
        "arrival_airport": "Mumbai Airport",
        "departure_time": "10:00",
        "arrival_time": "11:30",
        "price": 5000
    },
    "BA456": {
        "airline": "Air India",
        "departure_airport": "Pune International Airport",
        "arrival_airport": "Kempegowda International Airport",
        "departure_time": "12:00",
        "arrival_time": "14:00",
        "price": 9000
    },
    "LHT789": {
        "airline": "Air Asia",
        "departure_airport": "Shillong Airport",
        "arrival_airport": "Suvarnabhumi Airport",
        "departure_time": "18:00",
        "arrival_time": "22:00",
        "price": 25000
    }
}

departure_airport = input("Enter your departure airport: ")
arrival_airport = input("Enter your arrival airport: ")
flight_details = []
for flightNo, flightTime in flights.items():
    if flightTime["departure_airport"] == departure_airport and flightTime["arrival_airport"] == arrival_airport:
        flight_details.append(flightNo)
if flight_details:
    for flightNo in flight_details:
        flight = flights[flightNo]
        print("Flight number:", flightNo)
        print("Airline:", flight["airline"])
        print("Departure airport:", flight["departure_airport"])
        print("Arrival airport:", flight["arrival_airport"])
        print("Departure time:", flight["departure_time"])
        print("Arrival time:", flight["arrival_time"])
        print("Price:", flight["price"])
    flightNo = input("Enter the flight number you want to book: ")
    print ( f"flight {flightNo} booked successfully!")
else:
    print("No flights found!")

