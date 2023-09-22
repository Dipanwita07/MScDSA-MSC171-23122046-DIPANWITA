#create a class restaurant that accepts items and quantity as a input
#inside your class you are having the item and its price as a dictionary
#create a function and calculate cost that prints the item name, quantity and price

class restaurant:
    def __init__(self,item,qty):
        self.item = item
        self.qty = qty
        self.menu = {"rice" : 30, #members inside the class- init func and findcost func
            "chicken" : 100}
        
    def findCost(self):
        total =0
        total = self.qty*self.menu[self.item]
        print(self.item,self.qty,total) #self-current object
        
order = restaurant("rice",4)
order.findCost()

order2= restaurant("chicken",3)
order2.findCost()