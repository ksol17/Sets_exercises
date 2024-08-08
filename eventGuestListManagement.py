def remove_guest(guest_list):
    guest_name = input("Enter the guest name to remove: ")
    if guest_name in guest_list:
        guest_list.discard(guest_name)
        print(f"{guest_name} has been removed from the list.")
    else:
        print(f"{guest_name} not found in the guest list.")

def clear_guest_list(guest_list):
    guest_list.clear()
    print("The guest list has been cleared.")


def display_guest_list(guest_list):
    if guest_list:
        print("Current Guest List: ")
        for guest in guest_list:
            print(f"- {guest}")
    else:
        print("The guest list is currently empty.")



guest_list = {"Alice", "Bob", "Charlie", "Diana"}
while True:
    print("\n1. Remove a guest")
    print("2. Clear guest list")
    print("3. Display guest list")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        remove_guest(guest_list)
    elif choice == '2':
        clear_guest_list(guest_list)
    elif choice == '3':
        display_guest_list(guest_list)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again. ")