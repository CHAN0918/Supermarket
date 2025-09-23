import json
import os
from tabulate import tabulate

ITEMS_FILE = "items.json"

def load_items():
    if os.path.exists(ITEMS_FILE):
        with open(ITEMS_FILE, "r") as file:
            return json.load(file)
    return []

def save_items(items):
    with open(ITEMS_FILE, "w") as file:
        json.dump(items, file, indent=4)

def display_items():
    items = load_items()
    if not items:
        print("No items available.")
        return

    table = [[item["No"], item["Item"], f"{item['Price']:.2f}", item["Quantity"]] for item in items]
    headers = ["No", "Item", "Price (RM)", "Quantity"]
    print(tabulate(table, headers=headers, tablefmt="grid", colalign=("center", "left", "center", "left")))

def update_item():
    items = load_items()
    if not items:
        print("No items available.")
        return

    display_items()
    while True:
        choice = input("Enter item number to update (or 'C' to cancel): ").strip()
        if choice.lower() == 'c':
            return
        try:
            no = int(choice)
            for item in items:
                if item["No"] == no:
                    item["Item"] = input("New item name: ")
                    item["Price"] = float(input("New price (RM): "))
                    item["Quantity"] = input("New quantity: ")
                    save_items(items)
                    print("✅ Item updated.")
                    return
            print("❌ Item not found.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid number or 'C' to cancel.")

def workers_menu():
    while True:
        print("\n=== Workers Menu ===")
        print("1. Display Items")
        print("2. Update Item")
        print("3. Exit")

        choice = input("Select an option: ")
        if choice == "1":
            display_items()
        elif choice == "2":
            update_item()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    workers_menu()
