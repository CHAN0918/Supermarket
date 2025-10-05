import json
import os
from tabulate import tabulate

ITEMS_FILE = "Supermarket/items.json"

def load_items():
    if os.path.exists(ITEMS_FILE):
        with open(ITEMS_FILE, "r") as file:
            return json.load(file)
    return []

def display_items():
    items = load_items()
    if not items:
        print("No items available.")
        return

    table = [[item["No"], item["Item"], f"{item['Price']:.2f}", item["Quantity"]] for item in items]
    headers = ["No", "Item", "Price (RM)", "Quantity"]
    print(tabulate(table, headers=headers, tablefmt="grid", colalign=("center", "left", "center", "left")))

def add_to_cart(cart):
    items = load_items()
    if not items:
        print("No items to add.")
        return

    display_items()
    print("Press 'C' to cancel and return to main menu.")

    no_input = input("Enter item number to add to cart: ")
    if no_input.lower() == 'c':
        print("↩️ Returning to main menu.")
        return

    qty_input = input("Enter quantity to buy: ")
    if qty_input.lower() == 'c':
        print("↩️ Returning to main menu.")
        return

    try:
        no = int(no_input)
        quantity = int(qty_input)

        for item in items:
            if item["No"] == no:
                cart_item = {
                    "Item": item["Item"],
                    "Price": item["Price"],
                    "Quantity": quantity,
                    "Total": item["Price"] * quantity
                }
                cart.append(cart_item)
                print("🛒 Item added to cart.")
                return
        print("❌ Item not found.")
    except ValueError:
        print("⚠️ Invalid input.")

def view_cart(cart):
    if not cart:
        print("🛒 Cart is empty.")
        return

    table = [[i + 1, item["Item"], f"{item['Price']:.2f}", item["Quantity"], f"{item['Total']:.2f}"]
             for i, item in enumerate(cart)]
    headers = ["No", "Item", "Price (RM)", "Quantity", "Total (RM)"]
    print(tabulate(table, headers=headers, tablefmt="grid", colalign=("center", "left", "center", "center", "center")))

def checkout(cart):
    if not cart:
        print("🛒 Your cart is empty.")
        return

    view_cart(cart)
    total = sum(item["Total"] for item in cart)
    print(f"\n💰 Total to pay: RM {total:.2f}")
    print("Press 'C' to cancel and return to the main menu.\n")

    # Choose payment method
    print("Choose your payment method:")
    print("1. Cash")
    print("2. Debit/Credit Card")
    print("3. Touch 'n Go eWallet")
    print("4. GrabPay")
    
    method = input("Enter payment option (1-4 or 'C' to cancel): ")
    
    if method.lower() == 'c':
        print("↩️ Payment cancelled. Returning to main menu.")
        return

    # Payment Processing
    if method == '1':  # Cash
        cash_input = input("Enter cash amount (RM): ")
        if cash_input.lower() == 'c':
            print("↩️ Payment cancelled. Returning to main menu.")
            return
        try:
            cash = float(cash_input)
            if cash >= total:
                change = cash - total
                print(f"✅ Payment successful. Change: RM {change:.2f}")
                cart.clear()
            else:
                print("❌ Not enough cash.")
        except ValueError:
            print("⚠️ Invalid input. Payment failed.")

    elif method in ['2', '3', '4']:
        print("🔒 Processing payment securely...")
        # Simulate successful payment
        print("✅ Payment successful via", 
              "Card" if method == '2' else 
              "Touch 'n Go" if method == '3' else "GrabPay")
        cart.clear()

    else:
        print("⚠️ Invalid payment method selected.")



def customer_menu():
    cart = []
    while True:
        print("\n=== Customer Menu ===")
        print("1. Display Items")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Pay & Checkout")
        print("5. Exit")

        choice = input("Select an option: ")
        if choice == "1":
            display_items()
        elif choice == "2":
            add_to_cart(cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            checkout(cart)
        elif choice == "5":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    customer_menu()
