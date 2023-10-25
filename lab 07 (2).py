def menu():
    return [["Rice", 30],["Dal",60],["Chicken",130],["mutton",200]]
import random
def new_order():
    order_id = random.randint(1,1000)
    items = []
    while True:
        itemNo = ("Enter the item No:")
        if items == "0":
            break
        quantity = ("Enter the quantity")
        items.append({"item number": itemNo, "quantity": quantity})
        order = {"OrderId": order_id, "items": items}
        return order
    
def view_order():
   orders =[{
"OrderId": 56837,
"items": [
{
"itemNo": 2,
"quantity": 1,
},
    ]
    }
    ]
for order in orders:

       
def total_value(items):
    total_value = 0
    for item in items:
        total_value += item["price"] * item["quantity"]
    return total_value

def main():
    while True:
        print("Select an option:")
        print("1. Create new order")
        print("2. View orders")
        print("3. Exit")
        option = int(input("Enter your option: "))

        if option == 1:
            new_order()
        elif option == 2:
            view_order()
        elif option == 3:
            break
        else:
            print("Invalid option!")
main()
new_order()
view_order()
    

    
    
        
    
        