import json
import os
from tabulate import tabulate

ITEMS_FILE = "items.json"
WORKERS_FILE = "workers.json"

# ========== ITEM MANAGEMENT ==========

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

def add_item():
    items = load_items()
    item_name = input("Enter item name: ")
    price = float(input("Enter item price (RM): "))
    quantity = input("Enter quantity (e.g. 1 bottle, 5 packs): ")
    item_no = len(items) + 1
    items.append({
        "No": item_no,
        "Item": item_name,
        "Price": price,
        "Quantity": quantity
    })
    save_items(items)
    print("✅ Item added successfully.")
    input("Press C to return to main menu...")

def update_item():
    items = load_items()
    display_items()
    choice = input("Enter item number to update (or C to cancel): ")
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
                break
        else:
            print("❌ Item not found.")
    except ValueError:
        print("⚠️ Invalid input.")
    input("Press C to return to main menu...")

def remove_item():
    items = load_items()
    display_items()
    choice = input("Enter item number to remove (or C to cancel): ")
    if choice.lower() == 'c':
        return
    try:
        no = int(choice)
        items = [item for item in items if item["No"] != no]
        for idx, item in enumerate(items, start=1):
            item["No"] = idx
        save_items(items)
        print("🗑️ Item removed.")
    except ValueError:
        print("⚠️ Invalid input.")
    input("Press C to return to main menu...")

# ========== WORKER MANAGEMENT ==========

def load_workers():
    if os.path.exists(WORKERS_FILE):
        with open(WORKERS_FILE, "r") as file:
            return json.load(file)
    return []

def save_workers(workers):
    with open(WORKERS_FILE, "w") as file:
        json.dump(workers, file, indent=4)

def display_workers():
    workers = load_workers()
    if not workers:
        print("No workers found.")
        return

    table = [[w["id"], w["username"], w["position"], w["password"]] for w in workers]
    headers = ["ID", "Username", "Position", "Password"]
    print(tabulate(table, headers=headers, tablefmt="grid", colalign=("center", "center", "center", "center")))

def add_worker():
    workers = load_workers()
    username = input("Enter worker username: ")
    position = input("Enter worker position: ")
    worker_password = input("Enter worker password: ")
    worker_id = len(workers) + 1
    workers.append({
        "id": worker_id,
        "username": username,  
        "position": position,
        "password": worker_password
    })
    save_workers(workers)
    print("✅ Worker added.")
    input("Press C to return...")


def update_worker():
    workers = load_workers()
    display_workers()
    choice = input("Enter worker ID to update (or C to cancel): ")
    if choice.lower() == 'c':
        return
    try:
        worker_id = int(choice)
        for worker in workers:
            if worker["id"] == worker_id:
                worker["username"] = input("New username: ")  # ✅ FIXED
                worker["position"] = input("New position: ")
                worker["password"] = input("New worker password: ")
                save_workers(workers)
                print("✅ Worker updated.")
                break
        else:
            print("❌ Worker not found.")
    except ValueError:
        print("⚠️ Invalid input.")
    input("Press C to return...")

def remove_worker():
    workers = load_workers()
    display_workers()
    choice = input("Enter worker ID to remove (or C to cancel): ")
    if choice.lower() == 'c':
        return
    try:
        worker_id = int(choice)
        workers = [w for w in workers if w["id"] != worker_id]
        for idx, worker in enumerate(workers, start=1):
            worker["id"] = idx
        save_workers(workers)
        print("🗑️ Worker removed.")
    except ValueError:
        print("⚠️ Invalid input.")
    input("Press C to return...")

def manage_workers():
    while True:
        print("\n=== Manage Workers ===")
        print("1. Display Workers")
        print("2. Add Worker")
        print("3. Update Worker")
        print("4. Remove Worker")
        print("5. Return to Main Menu")

        choice = input("Choose option: ")
        if choice == "1":
            display_workers()
        elif choice == "2":
            add_worker()
        elif choice == "3":
            update_worker()
        elif choice == "4":
            remove_worker()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

# ========== ADMIN MENU ==========

def admin_menu():
    while True:
        print("\n=== Admin Menu ===")
        print("1. Display Items")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Manage Workers")  # <- moved up
        print("6. Exit")             # <- moved down

        choice = input("Select an option: ")
        if choice == "1":
            display_items()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            manage_workers()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    admin_menu()
