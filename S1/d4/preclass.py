def add_snack(inventory):
    snack_id = input("Enter the snack ID: ")
    snack_name = input("Enter the snack name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the snack available? (yes/no): ").lower()

    snack = {
        "snack_name": snack_name,
        "price": price,
        "availability": availability
    }

    inventory[snack_id] = snack
    print("Snack added to the inventory.")


def remove_snack(inventory):
    snack_id = input("Enter the snack ID to remove: ")

    if snack_id in inventory:
        del inventory[snack_id]
        print("Snack removed from the inventory.")
    else:
        print("Snack not found in the inventory.")


def update_availability(inventory):
    snack_id = input("Enter the snack ID to update availability: ")

    if snack_id in inventory:
        availability = input("Is the snack available? (yes/no): ").lower()
        inventory[snack_id]["availability"] = availability
        print("Availability updated.")
    else:
        print("Snack not found in the inventory.")


def record_sale(inventory, sales_records):
    snack_id = input("Enter the snack ID sold: ")

    if snack_id in inventory:
        snack = inventory[snack_id]
        if snack["availability"] == "yes":
            sales_records.append(snack_id)
            inventory[snack_id]["availability"] = "no"
            print("Sale recorded.")
        else:
            print("Snack is not available for sale.")
    else:
        print("Snack not found in the inventory.")


def print_inventory(inventory):
    print("Current Snack Inventory:")
    print("------------------------")
    for snack_id, snack in inventory.items():
        print(f"Snack ID: {snack_id}")
        print(f"Snack Name: {snack['snack_name']}")
        print(f"Price: {snack['price']}")
        print(f"Availability: {snack['availability']}")
        print("------------------------")


def print_sales_records(sales_records):
    print("Sales Records:")
    print("------------------------")
    if sales_records:
        for i, snack_id in enumerate(sales_records, start=1):
            print(f"Sale {i}: Snack ID {snack_id}")
    else:
        print("No sales records found.")
    print("------------------------")


def main():
    inventory = {}
    sales_records = []

    while True:
        print("Snack Inventory Management")
        print("--------------------------")
        print("1. Add a snack to inventory")
        print("2. Remove a snack from inventory")
        print("3. Update snack availability")
        print("4. Record a sale")
        print("5. Print inventory")
        print("6. Print sales records")
        print("7. Quit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_snack(inventory)
        elif choice == "2":
            remove_snack(inventory)
        elif choice == "3":
            update_availability(inventory)
        elif choice == "4":
            record_sale(inventory, sales_records)
        elif choice == "5":
            print_inventory(inventory)
        elif choice == "6":
            print_sales_records(sales_records)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


main()
