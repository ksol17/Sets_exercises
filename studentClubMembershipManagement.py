def add_member(clubs, club_name, member_name):
    if club_name in club_name:
        clubs[club_name].add(member_name)
        print(f"{member_name} has been added to {club_name}.")
    else:
        print(f"Club {club_name} not found.")


def remove_member(clubs, club_name, member_name):
    if club_name in clubs and member_name in clubs[club_name]:
        clubs[club_name].remove(member_name)
        print(F"{member_name} has been removed from {club_name}.")
    else:
        print(f"Member not found.")

def display_membership(clubs):
    for club, members in clubs.items():
        print(f"{club} Members: {', '.join(members)}")



clubs = {
    "Art Club": {"Alice", "Bob"},
    "Book Club": {"Charlie", "Diana"}
}

while True:
    print("\n1. Add a member")
    print("2. Remove a member")
    print("3. Display memberships")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        club_name = input("Enter the club name: ")
        member_name = input("Enter the member's name: ")
        add_member(clubs, club_name, member_name)
    elif choice == '2':
        club_name = input("Enter the club name: ")
        member_name = input("Enter the member's name: ")
        remove_member(clubs, club_name, member_name)
    elif choice == '3':
        display_membership(clubs)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")