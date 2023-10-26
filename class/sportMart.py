class sportMart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}
    def createInventory(self,ProductID,ProductName,Quantity,price):
        temp ={
            "productid": ProductID,
            "productname": ProductName,
            "quantity": Quantity,
            "price": price
        }
        self.inventory[ProductID] = temp
    def createOrder(self,OrderID,ProductID,Quantity,price,Total):
        temp = {
            "orderID":OrderID,
            "productid": ProductID,
            "quantity":  Quantity,
            "price": price,
            "total": Total
        }
        self.orders[OrderID] = temp
    def printOrders(self):
        print(self.orders)
    def printInventory(self):
        print(self.inventory)
trinity = sportMart()
orders = open('orders.csv','r')
o_header = orders.readline()
o_data = orders.readlines()
for data in o_data:
    tmp = data.strip().split(',')
    trinity.createOrder(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])
trinity.printOrders()

inventory = open('inventory.csv','r')
i_header = inventory.readlines()
i_data = inventory.readlines()
for data in i_data:
    tmp = data.strip().split(',')
    trinity.createInventory(tmp[0],tmp[1],tmp[2],tmp[3])
trinity.printInventory()
def main():
    trinity= sportMart()
    trinity.inventory()
    trinity.orders()

while True:
    print("\nSportMart Menu:")
    print("1. Display Inventory")
    print("2. Display Order History")
    print("3. Add Item to Inventory")
    print("4. Place Order")
    print("5. Exit")
    store = []
    order =[]
    choice = input("Enter your choice: ")
    if choice == "1":
            trinity.inventory()
    elif choice == "2":
            trinity.orders()
    elif choice == "3":
            ProductID = input("Enter item ID: ")
            ProductName = (input("Enter item name: "))
            Quantity = int(input("Enter item quantity: "))
            price = float(input("enter the product price:"))
            trinity_product = sportMart(ProductID,ProductName,Quantity,price)
            store.append(trinity_product)
    elif choice == "4":
            OrderID = input("Enter customer order ID: ")
            ProductID = input("Enter item ID: ")
            Quantity = int(input("Enter item quantity: "))
            price = float(input("enter the product price:"))
            Total = price*Quantity
            trinity_order=sportMart(OrderID,ProductID,Quantity,price,Total)
            order.append(trinity_order)
    elif choice == "5":
            trinity.inventory()
            trinity.orders()
            print("Exit")
            break
    else:
            print("Invalid choice")