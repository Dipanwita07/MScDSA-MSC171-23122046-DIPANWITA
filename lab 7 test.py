import random

# Define a function to generate a random order ID
def generate_order_id():
    return "".join([str(random.randint(1, 9)) for i in range(5)])

# Define a function to get the menu items and their prices
def get_menu():
    return [["Rice", 30], ["Tea", 10], ["Chicken Biriyani", 150], ["Mutton Biriyani", 200]]

# Define a function to create a new order
def create_order():
    order_id = generate_order_id()
    items = []
    while True:
        item_number = input("Enter the item number: ")
        if item_number == "0":
            break
        quantity = input("Enter the quantity: ")
        items.append({"itemnumber": item_number, "quantity": quantity})
    order = {"Orderid": order_id, "items": items}
    return order

# Define a function to view all orders
def view_orders():
    orders = []
    with open("orders.txt", "r") as f:
        orders = json.load(f)
    for order in orders:
        print(order)

# Define a function to calculate the total order value
def calculate_order_value(order):
    total_value = 0
    for item in order["items"]:
        total_value += get_menu()[item["itemnumber"]]["price"] * item["quantity"]
    return total_value

# Define the main function
def main():
    while True:
        print("Select an option:")
        print("1. Create new order")
        print("2. View orders")
        print("3. Exit")
        option = int(input("Enter your option: "))

        if option == 1:
            order = create_order()
            with open("orders.txt", "a") as f:
                json.dump(order, f)
        elif option == 2:
            view_orders()
        elif option == 3:
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
