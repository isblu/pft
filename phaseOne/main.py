import json
from time import sleep
from tabulate import tabulate
import txt

# Global list to store transactions
transactions = []

def load_transactions():
    global transactions
    try:
        with open("phaseOne\\transactions.json") as file:
            transactions = json.load(file)
    except:
        with open("phaseOne\\transactions.json", "w") as file:
            pass

def save_transactions():
    global transactions
    while True:
        try:
            choice = input("\nSave changes? (Y/N): ")
            choice = choice.upper()
            if choice == "Y":
                with open("phaseOne\\transactions.json", "w") as f:
                    json.dump(transactions, f, indent=3)
                print("\nChanges saved!")
                break
            if choice == "N":
                break
        except:
            print("\nInvalid input!")
            continue

    if choice == "N":
        main_menu()

    input("\nPress any key to go back...")
    main_menu()

# Feature implementations
def add_transaction():
    global transactions
    print(txt.add)

    record = []
    record.append(len(transactions) + 1)

    while True:
        try:
            amount = float(input("(0 to go back) Enter transaction amount (Rs.): "))
            if amount == 0.0:
                break
            record.append(amount)
            break
        except:
            continue

    if amount == 0.0:
        main_menu()

    while True:
        try:
            category = input("Enter transaction category: ")
            record.append(category)
            break
        except:
            continue

    while True:
        try:
            transaction_type = input("Enter transaction type (Income/Expense): ")
            record.append(transaction_type)
            break
        except:
            continue

    while True:
        try:
            transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
            record.append(transaction_date)
            break
        except:
            print("Invalid Date!")
            continue

    transactions.append(record)
    save_transactions()

def view_transactions():
    global transactions
    print(txt.view)
    print(tabulate(transactions, headers=["No.", "Amount (Rs.)", "Category", "transaction_type", "Date"], tablefmt="rounded_grid"))
    input("\nPress any key to go back...")
    main_menu()

def update_transaction():
    global transactions
    print(txt.update)
    while True:
        choice = int(input("(0 to go back) Enter transaction number: "))
        if choice == 0:
            break
        else:
            if 0 < choice <= len(transactions):
                break
            else:
                print("Invalid transaction number!")
                continue
    
    if choice == 0:
            main_menu()

    print(tabulate([transactions[choice-1]], headers=["No.", "Amount (Rs.)", "Category", "transaction_type", "Date"], tablefmt="rounded_grid"))
    while True:
        try:
            amount = float(input(f"(0 to go back) Change {transactions[choice-1][1]} to (Rs.): "))
            if amount == 0:
                break
            elif amount == "":
                break
            else:
                transactions[choice-1][1] = amount
                break
        except:
            continue

    if amount == 0:
        update_transaction()

    while True:
        try:
            category = input(f"Change {transactions[choice-1][2]} to: ")
            if category == "":
                break
            else:
                transactions[choice-1][2] = category
                break
        except:
            continue

    while True:
        try:
            transaction_type = input(f"Change {transactions[choice-1][3]} to: ")
            if transaction_type == "":
                break
            else:
                transactions[choice-1][3] = transaction_type
                break
        except:
            continue

    while True:
        try:
            transaction_date = input(f"Change {transactions[choice-1][4]} to (YYYY-MM-DD): ")
            if transaction_date == "":
                break
            else:
                transactions[choice-1][4] = transaction_date
                break
        except:
            continue

    print(tabulate([transactions[choice-1]], headers=["No.", "Amount", "Category", "transaction_type", "Date"], tablefmt="rounded_grid"))

    save_transactions()

def delete_transaction():
    global transactions
    print(txt.remove)

    while True:
        choice = int(input("(0 to go back) Enter transaction number: "))
        if choice == 0:
            break
        else:
            choice = int(choice)
            if 0 < choice <= len(transactions):
                break
            else:
                print("Invalid transaction number!")
                continue

    if choice == 0:
            main_menu()

    print(tabulate([transactions[choice-1]], headers=["No.", "Amount (Rs.)", "Category", "transaction_type", "Date"], tablefmt="rounded_grid"))
    confirm = None
    looping = True

    while looping:
        if not confirm == "y" or confirm == "n":
            confirm = input("\nDelete Entry? (y/n): ").lower()
        looping = False

    if confirm == "y":
        transactions.pop(choice-1)
        print("\nTransaction removed!")

        for i in range(choice-1, len(transactions)):
            transactions[i][0] = transactions[i][0]-1
    if confirm == "n":
        main_menu()

    save_transactions()

def display_summary():
    global transactions
    print(txt.summary)
    print(f" > Number of transactions: {len(transactions)}")
    input("\nPress any key to go back...")
    main_menu()

def main_menu():
    global file
    print(txt.menu)

    load_transactions()

    while True:
        try:
            choice = int(input(" >>> "))
            if 0 <= choice < 6:
                break
        except:
            print("Invalid input!")
            continue

    if choice == 1:
        add_transaction()
    if choice == 2:
        view_transactions()
    if choice == 3:
        update_transaction()
    if choice == 4:
        delete_transaction()
    if choice == 5:
        display_summary()
    if choice == 0:
        print("Yeetus deletus the fetus...")
        sleep(0.5)
        exit()

if __name__ == "__main__":
    main_menu()