import json
import os
import getpass
import subprocess

# File paths
ADMIN_FILE = "admins.json"
WORKER_FILE = "workers.json"

def load_users(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

def login_admin():
    users = load_users(ADMIN_FILE)
    while True:
        print("\n--- Admin Login ---")
        username = input("Enter admin username (or press C to return): ")
        if username.lower() == 'c':
            return
        password = getpass.getpass("Enter password: ")

        for user in users:
            if user["username"] == username and user["password"] == password:
                print("✅ Admin login successful!")
                subprocess.run(["python", "admin.py"])
                return
        print("❌ Invalid admin credentials. Please try again.")

def login_worker():
    users = load_users(WORKER_FILE)
    while True:
        print("\n--- Worker Login ---")
        username = input("Enter worker username (or press C to return): ")
        if username.lower() == 'c':
            return
        password = getpass.getpass("Enter password: ")

        for user in users:
            if user["username"] == username and user["password"] == password:
                print("✅ Worker login successful!")
                subprocess.run(["python", "workers.py"])
                return
        print("❌ Invalid worker credentials. Please try again.")

def main_menu():
    while True:
        print("\n=== Login Menu ===")
        print("1. Admin Login")
        print("2. Worker Login")
        print("3. Customer (no login required)")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            login_admin()
        elif choice == "2":
            login_worker()
        elif choice == "3":
            subprocess.run(["python", "Customer.py"])
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
