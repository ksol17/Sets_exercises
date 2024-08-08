def add_product(inventory):
    product_name = input("Enter the product name: ")
    category = input("Enter the product category: ")
    product = (product_name, category)

    if product in inventory:
        print(f"{product_name} already exists in the inventory.")
    else:
        inventory.add(product)
        print(f"{product_name} added to inventory.")



def update_product(inventory):
    product_name = input("Enter the product name to update: ")
    new_category = input("Enter the new category: ")
    product_found = False

    for product in inventory:
        print(product)
        if product[0] == product_name:
            inventory.remove(product)
            inventory.add((product_name, new_category))
            product_found = True
            print(f"{product_name} has been updated to {new_category} category.")
            break
    if not product_found:
        print(f"{product_name} not found in the inventory.")

def display_inventory(inventory):
    print("Current Inventory:")
    for product in inventory:
        print(f"Product: {product[0]}, Category: {product[1]}")










inventory = set()
while True:
    print("\n1. Add a product")
    print("2. Update a product")
    print("3. Display inventory")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_product(inventory)
    elif choice == '2':
        update_product(inventory)
    elif choice == '3':
        display_inventory(inventory)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again. ")