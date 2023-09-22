import csv


class expenseTracker:
    def _init_(self, csv_filename):
        self.expenseDict = {
            "income": [],
            "expense": [],
        }
        self.csv_filename = csv_filename

        # Create the CSV file and write the header if it doesn't exist
        with open(self.csv_filename, mode="a+", newline="") as file:
            expense = expense.csv (file)
            # Check if the file is empty and write the header if needed
            if file.tell() == 0:
                expense.writerow([ "Category", "Cost" "Description","Date", "Type"])

    def store_transactions(self, type, category, cost, desc,date):
        trans = {
            "Category":category,
            "cost":cost,
            "Description":desc,
            "Date":date
        }
        if type == "income":
            self.expenseDict["income"].append(trans)
            transaction_type = "Income"
        else:
            self.expenseDict["expense"].append(trans)
            transaction_type = "Expense"

        # Add the transaction to the CSV file with the transaction type
        self.add_transaction_to_csv( category, cost, desc, date)

    def view_transactions(self):
        print("Your Income:")
        for item in self.expenseDict["income"]:
            print(item)
        print("Your Expenses:")
        for item in self.expenseDict["expense"]:
            print(item)

    def calculate_transactions(self):
        total_income = sum(item["Amount"] for item in self.expenseDict["income"])
        total_expense = sum(item["Amount"] for item in self.expenseDict["expense"])
        print("Total Income\t:\t", total_income)
        print("Total Expenses\t:\t", total_expense)

    def add_transaction_to_csv(self, category,cost, desc,  date):
        with open(self.csv_filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([category, cost, desc, date,])


def collectInput():
    cost = int(input("Enter the cost: "))
    category = input("Enter Category: ")
    date = input("Enter Date (DD/MM/YYYY): ")
    desc = input("Enter the description: ")
    return cost, category, date, desc


myExpense = expenseTracker("expense_records.csv")

while True:
    print("...MY EXPENSE TRACKER...")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Records")
    print("4. View My Spending")
    print("5. Exit")

    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        print("Enter the details of income")
        category,cost, date, desc = collectInput()
        myExpense.store_transactions("income", category,cost, date, desc)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = collectInput()
        myExpense.store_transactions ("expense", category,cost, date, desc)
    elif choice == 3:
        myExpense.view_transactions()
    elif choice == 4:
        myExpense.calculate_transactions()
    elif choice == 5:
        exit()
    else:
        print("Invalid choice")


