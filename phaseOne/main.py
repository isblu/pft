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
                    json.dump(transactions, f)
                print("\nTransaction added!")
                break
            if choice == "N":
                main_menu()
                break
        except:
            print("\nInvalid input!")
            continue
    
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
            amount = float(input("Enter transaction amount (Rs.): "))
            record.append(amount)
            break
        except:
            continue
    
    while True:
        try:
            category = input("Enter transaction category: ")
            record.append(category)
            break
        except:
            continue

    while True:
        try:
            type = input("Enter transaction type (Income/Expense): ")
            record.append(type)
            break
        except:
            continue
    
    while True:
        try:
            date = input("Enter transaction date: ")
            record.append(date)
            break
        except:
            continue
    
    transactions.append(record)

    save_transactions()

def view_transactions():
    global transactions
    print(txt.view)
    print(tabulate(transactions, headers=["No.", "Amount", "Category", "Type", "Date"], tablefmt="rounded_grid"))
    input("\nPress any key to go back...")
    main_menu()

def update_transaction():
    global transactions
    print(txt.update)
    while True:
        choice = input("Enter transaction number (Non-numeric values sends you back!): ")
        if choice.isnumeric() == False:
            main_menu()
            break
        else:
            choice = int(choice)
            if 0 < choice <= len(transactions):
                break
            else:
                print("Invalid transaction number!")
                continue

    while True:
        try:
            amount = float(input(f"(0 to go back) Change {transactions[choice-1][1]} to (Rs.): "))
            if amount == 0:
                update_transaction()
                break
            else:
                transactions[choice-1][1] = amount
                break
        except:
            continue
    
    while True:
        try:
            category = input(f"(0 to go back) Change {transactions[choice-1][2]} to: ")
            if category == "0":
                update_transaction()
                break
            else:
                transactions[choice-1][2] = category
                break
        except:
            continue
    
    while True:
        try:
            type = input(f"(0 to go back) Change {transactions[choice-1][3]} to: ")
            if type == "0":
                update_transaction()
                break
            else:
                transactions[choice-1][3] = type
                break
        except:
            continue

    while True:
        try:
            date = input(f"(0 to go back) Change {transactions[choice-1][4]} to (YYYY-MM-DD): ")
            if date == "0":
                update_transaction()
                break
            else:
                transactions[choice-1][4] = date
                break
        except:
            continue

    save_transactions()

def delete_transaction():
    global transactions
    print(txt.remove)

    while True:
        choice = input("Enter transaction number (Non-numeric values sends you back!): ")
        if choice.isnumeric() == False:
            main_menu()
            break
        else:
            choice = int(choice)
            if 0 < choice <= len(transactions):
                break
            else:
                print("Invalid transaction number!")
                continue
    
    print(f"Selected transaction: {", ".join(str(x) for x in transactions[choice-1])}")
    
    while True:
        try:
            confirm = input("\nDelete Entry? (Y/N): ")
            confirm = confirm.upper()
            if confirm == "Y":
                transactions.pop(choice-1)
                print("\nTransaction removed!")

                for i in range(len(transactions)):
                    transactions[i][0] = transactions[i][0]-1
                break
            if choice == "N":
                main_menu()
                break
        except:
            print("\nInvalid input!")
            continue
    
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
            if 0 < choice < 6:
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
        print("Yeetus deletus the fetus...")
        sleep(1)
        exit()

if __name__ == "__main__":
    main_menu()