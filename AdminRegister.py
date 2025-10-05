import json
import os
import getpass

ADMINS_FILE = "Supermarket/admins.json"

def load_admins():
    if os.path.exists(ADMINS_FILE):
        with open(ADMINS_FILE, "r") as file:
            return json.load(file)
    return []

def save_admins(admins):
    with open(ADMINS_FILE, "w") as file:
        json.dump(admins, file, indent=4)

def display_admins():
    admins = load_admins()
    if not admins:
        print("⚠️ No admins registered.")
    else:
        print("\n=== Registered Admins ===")
        for i, admin in enumerate(admins, start=1):
            print(f"{i}. {admin['username']}")
        print()

def register_admin():
    admins = load_admins()
    username = input("Enter new admin username (or press C to return): ")
    if username.lower() == 'c':
        return

    if any(admin["username"] == username for admin in admins):
        print("⚠️ Username already exists.")
        return

    while True:
        password = getpass.getpass("Enter password: ")
        confirm = getpass.getpass("Confirm password: ")
        if password == confirm:
            break
        else:
            print("❌ Passwords do not match. Try again.")

    admins.append({"username": username, "password": password})
    save_admins(admins)
    print("✅ Admin registered successfully.")

def update_admin():
    admins = load_admins()
    display_admins()
    username = input("Enter username to update (or press C to return): ")
    if username.lower() == 'c':
        return

    for admin in admins:
        if admin["username"] == username:
            new_username = input("Enter new username: ")
            new_password = getpass.getpass("Enter new password: ")
            admin["username"] = new_username
            admin["password"] = new_password
            save_admins(admins)
            print("✅ Admin updated.")
            return

    print("❌ Admin not found.")

def remove_admin():
    admins = load_admins()
    display_admins()
    username = input("Enter username to remove (or press C to return): ")
    if username.lower() == 'c':
        return

    updated_admins = [admin for admin in admins if admin["username"] != username]
    if len(updated_admins) == len(admins):
        print("❌ Admin not found.")
    else:
        save_admins(updated_admins)
        print("🗑️ Admin removed.")

def admin_register_menu():
    while True:
        print("\n=== Admin Registration Menu ===")
        print("1. Display Admins")
        print("2. Register Admin")
        print("3. Update Admin")
        print("4. Remove Admin")
        print("5. Exit")

        choice = input("Choose option: ")
        if choice == "1":
            display_admins()
        elif choice == "2":
            register_admin()
        elif choice == "3":
            update_admin()
        elif choice == "4":
            remove_admin()
        elif choice == "5":
            print("Exiting Admin Registration Menu.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    admin_register_menu()
