import json

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    try:
        with open('transactions.json', 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        with open('transactions.json', 'r') as f:
            return f.read()

def save_transactions(transactions):
    with open('transactions.json', 'a+') as f:
        json.dumps(transactions, f)
        print("The data stored succesfully")

# Feature implementations
def add_transaction():
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    type = input("Enter the type (Income/Expense): ")
    date = input("Enter the date (YYYY-MM-DD): ")
    transactions.append = [amount, category, type, date]
    save_transactions(transactions)

def view_transactions():
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
            if transactions:
                print("Transactions:")
                for index, transaction in enumerate(transactions, start=1):
                    print(f"{index}. {transaction['description']}: ${transaction['amount']}")
            else:
                print("No transactions found.")
    except FileNotFoundError:
        print("No transactions found.")



def update_transaction():
    index = int(input("Enter the index of the transaction to update: "))
    transactions[index] = add_transaction()
    save_transactions(transactions)

def delete_transaction():
    index = int(input("Enter the index of the transaction to delete: "))
    del transactions[index]
    save_transactions(transactions)

def display_summary():
    income = sum(transaction[0] for transaction in transactions if transaction[2] == "Income")
    expense = sum(transaction[0] for transaction in transactions if transaction[2] == "Expense")
    print(f"Total Income: {income}")
    print(f"Total Expense: {expense}")

def main_menu():
    load_transactions()
    while True:
        print("\n===== Personal Finance Tracker =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main_menu()