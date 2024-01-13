class Item:
    def __init__(self, name, code, price, stock, category):
        #initialize item properties
        self.name = name
        self.code = code
        self.price = price
        self.stock = stock
        self.category = category

class Category:
    def __init__(self, code, name, items):
        #initialize category properties
        self.code = code
        self.name = name
        self.items = items

print("🌟 WELCOME TO MINUTE STOP 🌟\n")

def print_menu(categories, hide_category=False):
    # Function to print the menu of categories
    if not hide_category:
        for category in categories:
            print(f"{category.code}:\t{category.name}")

def print_items_in_category(category):
    # Function to print items within a specific category
    print(f"\n\nItems in {category.name} category:\n")
    for item in category.items:
        print(f"{item.code} - {item.name}|\nPrice: ${item.price} | \nStock: {item.stock}\n")

def order_category(categories, code):
    # Function to order a category or item based on user input
    for category in categories:
        for item in category.items:
            if item.code.lower() == code.lower():
                return item
        if category.code.lower() == code.lower():
            return category
    return None

def calculate_change(price, amount_paid):
    # Function to calculate the change during payment
    if amount_paid < price:
        return None
    return round(amount_paid - price, 2)

def print_receipt(selected_items):
    # Function to print a receipt with selected items and total price
    print("\nYour order is being prepared!")
    print("\nReceipt:")
    total_price = 0
    for selected_item in selected_items:
        print(f"{selected_item['quantity']} - {selected_item['name']} - ${selected_item['price']:.2f}")
        total_price += selected_item['price']
    print(f"\nTotal --- ${round(total_price, 2)}\n")

def insert_money_again(selected_items):
    # Function to handle insufficient money during payment
    while True:
        additional_amount = float(input("\n❌ Insufficient Amount \n\tInsert additional money: "))
        if additional_amount > 0:
            amount_paid = float(input("\nYour remaining total is ${:.2f}\n\tHow much additional money: ".format(
                sum(item['price'] for item in selected_items) - additional_amount)))

            if amount_paid >= sum(item['price'] for item in selected_items):
                change = calculate_change(sum(item['price'] for item in selected_items), amount_paid)
                print(f"\n💸 Received ${amount_paid}, your change is ${round(change, 2)}.")
                print_receipt(selected_items)
                print(" Thank you for choosing Minute Stop!")
                return True
            else:
                print("\n❌ Insufficient funds. Please try again.")
        else:
            print("\nThank you for stopping by!")
            return False

def main():
    # Function to simulate the store experience
    Mango_Drinks = [Item("Mango Classic Smoothie", "M1", 3.99, 10, "Mango"),
                    Item("Mango Graham Shake", "M2", 4.59, 15, "Mango"),
                    Item("Mango Sparkle", "M3", 2.99, 10, "Mango")]

    Avocado_Drinks = [Item("Avocado Classic Smoothie", "A1", 3.99, 10, "Avocado"),
                      Item("Avocado Graham Shake", "A2", 4.59, 15, "Avocado"),
                      Item("Signature Avocado", "A3", 2.99, 10, "Avocado")]

    Snacks = [Item("Clover Chips", "S1", 1.49, 5, "Chips"),
              Item("Doritos", "S2", 2.49, 5, "Chips")]

    Pastries = [Item("Chocolate Croissant", "P1", 2.49, 10, "Pastry"),
                Item("Blueberry Cheesecake", "P2", 3.99, 10, "Pastry")]

    categories = [
        Category("1", "Mangos🥭", Mango_Drinks),
        Category("2", "Avocado🥑", Avocado_Drinks),
        Category("3", "Chips✨", Snacks),
        Category("4", "Pastry 🥮", Pastries)
    ]

    in_category_section = False  # Flag to track the user's current state
    selected_items = []

    while True:
        print_menu(categories, hide_category=in_category_section)

        if not in_category_section:
            code_category = input("\nExplore category | '0' to quit:")
            if code_category == '0':
                print("\nThank you for stopping by!")
                break

            item_category = order_category(categories, code_category)

            if isinstance(item_category, Category):
                category = item_category
                print_items_in_category(category)
                in_category_section = True  # Set the flag to True when entering the category section
            else:
                print("\nInvalid category code. Please try again.")
        else:
            code = input("\nEnter code of the item | \n'c' to go back to categories | \n'0' to quit:")
            if code.lower() == 'c':
                print("\nGoing back to categories page.")
                in_category_section = False
                continue
            elif code == '0':
                print("\nThank you for stopping by!")
                break

            item_category = order_category(categories, code)

            if isinstance(item_category, Item):
                item = item_category
                quantity = int(input(f"\nHow many {item.name}s would you like to buy? (Available: {item.stock}): "))
                if quantity > item.stock:
                    print("\nInsufficient stock. Please enter a quantity within the available stock.")
                    continue

                selected_items.append({'name': item.name, 'price': item.price * quantity, 'quantity': quantity})
                item.stock -= quantity  # Deduct the purchased quantity from the stock
                print(f"\nYou selected:\n\t{quantity} {item.name} - ${item.price * quantity:.2f}")

                follow_up = input("\nDo you want to pay now or order more? (P/O): ").lower()
                if follow_up == "p":
                    print("\n💳 Proceed to checkout:")
                    amount_paid = float(input("\nYour total is ${:.2f}\n\tPayment received: ".format(
                        sum(item['price'] for item in selected_items))))

                    if amount_paid < sum(item['price'] for item in selected_items):
                        if not insert_money_again(selected_items):
                            break
                    else:
                        change = calculate_change(sum(item['price'] for item in selected_items), amount_paid)
                        print(f"\n💸 Received ${amount_paid}, your change is ${round(change, 2)}.")
                        print_receipt(selected_items)
                        print(" Thank you for choosing Minute Stop!")
                        break

if __name__ == "__main__":
    main()