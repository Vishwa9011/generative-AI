

def showInventory(inventory, orders):
    for id, dish in inventory.items():
        print(f"{id}. {dish}")


def add_dish(inventory, orders):
    id = input("Enter the ID of Dish: ")
    dish_name = input("Enter the name of Dish: ")
    dish_stock = int(input("Enter the stock of Dish: "))
    price = int(input("Enter the price of Dish: "))

    inventory[id] = {
        "dish_name": dish_name,
        "dish_stock": dish_stock,
        "availibility": "yes",
        "price": price
    }
    showInventory()


def remove_dish(inventory, orders):
    id = int(input("Enter the ID to remove dish: "))
    if id in inventory:
        del inventory[id]
    else:
        print("Enter ID is not available.")


# Update the availability of a dish based on their dynamic kitchen operations.
def update_dish(inventory, orders):
    id = int(input("Enter ID to update the availibility: "))
    if id in inventory:
        stock = int(input("Enter the new stock value: "))
        if (stock > 0):
            inventory[id]["dish_stock"] = stock
            inventory[id]["availability"] = "yes"
        else:
            inventory[id]["dish_stock"] = 0
            inventory[id]["availability"] = "no"
    else:
        print("Id not Found")


def take_new_order(inventory, orders):
    id = int(input("Enter ID of dish, you want to purchase: "))
    if id in inventory:
        order_amount = int(input("Enter the amount you want to purchase: "))
        id = int(input("Enter the Order ID: "))
        customer_name = input("Enter your name: ")

        if order_amount < inventory[id]["dish_stock"]:
            inventory[id]["dish_stock"] -= order_amount
            orders[id] = {
                "customer_name": customer_name,
                "order_amount": order_amount,
                "order_status": "received"
            }
        else:
            print("Order amount is not available. please try to order in minimum amount")
    else:
        print("Dish not found")


def update_order_status(inventory, orders):
    id = int(input("Enter ID of order ID, you want to update: "))
    if id in orders:
        print()
        print("Press 1, For preparing")
        print("Press 2, For received")
        print("Press 3, For delivered")
        print()

        status_key = int(input("Enter the key for new order status: "))

        if status_key == 1:
            orders[id]["order_status"] = "preparing"
            print("Order status has been changed to preparing")
        elif status_key == 2:
            orders[id]["order_status"] = "received"
            print("Order status has been changed to received")
        elif status_key == 3:
            orders[id]["order_status"] = "delivered"
            print("Order status has been changed to delivered")
        else:
            print("Sorry please try again, you have enterd wrong status key")
    else:
        print("-----order not found---")


def show_sales_records(inventory, orders):
    for id, sale_item in orders.items():
        print(f"{id}: {sale_item}")


def main():
    inventory = {
        1: {
            "price": 10,
            "dish_stock": 19,
            "dish_name": "samosa",
            "availibility": "yes"
        },
    }

    orders = {}

    while True:
        print("------------------------------------------")
        print("----Zomato Inventory management system---")
        print("------------------------------------------")
        print("1. Add a dish to inventory")
        print("2. Remove a dish from inventory")
        print("3. Update dish availability")
        print("4. Take a new order.")
        print("5. Update the order status")
        print("6. Print sales records")
        print("7. Show Inventory")
        print()
        user_input = int(input("Enter your choice: "))

        if user_input == 1:
            add_dish(inventory, orders)
        elif user_input == 2:
            remove_dish(inventory, orders)
        elif user_input == 3:
            update_dish(inventory, orders)
        elif user_input == 4:
            take_new_order(inventory, orders)
        elif user_input == 5:
            update_order_status(inventory, orders)
        elif user_input == 6:
            show_sales_records(inventory, orders)
        elif user_input == 7:
            showInventory(inventory, orders)


if __name__ == '__main__':
    main()
