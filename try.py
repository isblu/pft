import json

def load_transactions():
    global transactions
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        # If file not found, initialize transactions list
        transactions = []

def save_transactions():
    with open('transactions.json', 'w') as file:
        json.dumps(transactions, file)

def add_transaction():
    description = input("Enter transaction description: ")
    amount = float(input("Enter transaction amount: "))
    transactions.append({"description": description, "amount": amount})
    save_transactions()
    
def view_transactions():
    for index, transaction in enumerate(transactions, start=1):
        print(f"{index}. {transaction['description']}: ${transaction['amount']}")

def update_transaction():
    view_transactions()
    try:
        index = int(input("Enter the index of the transaction to update: ")) - 1
        description = input("Enter new description (leave blank to keep current): ")
        amount = input("Enter new amount (leave blank to keep current): ")
        if description:
            transactions[index]['description'] = description
        if amount:
            transactions[index]['amount'] = float(amount)
        save_transactions()
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid index.")

def delete_transaction():
    view_transactions()
    try:
        index = int(input("Enter the index of the transaction to delete: ")) - 1
        del transactions[index]
        save_transactions()
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid index.")

def display_summary():
    total_income = sum(transaction['amount'] for transaction in transactions if transaction['amount'] > 0)
    total_expense = sum(transaction['amount'] for transaction in transactions if transaction['amount'] < 0)
    print(f"Total Income: ${total_income}")
    print(f"Total Expense: ${total_expense}")
    print(f"Net Balance: ${total_income + total_expense}")

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
