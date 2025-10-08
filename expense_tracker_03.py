expenses = []

def add_expense():
    item = input("Input item: ").strip()
    if not item:
        print("No item entered")
        return
    while True:
        try:
            value = float(input("Input value: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    expenses.append({"item": item, "value": value})
    print(f"Added '{item}' for ${value:,}")

def view_expenses():
    if not expenses:
        print("No expenses have been added yet.")
    else:
        for i in expenses:
            print(f"{i["item"]}: ${i["value"]:,}")
        
def total_expenses():
    if not expenses:
        print("No expenses have been added yet.")
    else:
        print(f"Total Expenses: ${sum(i["value"] for i in expenses):,}")

def clear_expenses():
    expenses.clear()
    print("Expenses cleared.")
    

while True:
    print("\n1. Add | 2. View | 3. Total | 4. Clear | 5. Exit")
    try:
        selection = int(input("Choose option: "))
    except:
        print("Please input a valid number.")
        continue

    match selection:
        case 1: add_expense()
        case 2: view_expenses()
        case 3: total_expenses()
        case 4: 
            confirmation = input("Clear all expenses? (y/n): ").lower()
            if confirmation == "y":
                clear_expenses()
            else:
                print("Clear canceled.")
        case 5: 
            print("Quitting program.")
            break
        case _: print("Invalid selection.")
    
    