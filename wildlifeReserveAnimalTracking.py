def perform_set_operation(zones, operation, zone1, zone2=None):
    zone1_animals = zones.get(zone1, set())
    zone2_animals = zones.get(zone2, set()) if zone2 else set()

    if operation == 'union':
        result = zone1_animals.union(zone2_animals)
        print(result)
    elif operation == 'intersection':
        result = zone1_animals.intersection(zone2_animals)
        print(result)
    elif operation == 'difference':
        result == zone1_animals.difference(zone2_animals)
        print(result)
    else:
        print("Invalid operation")




zones = {
    "ZoneA": {"lion", "elephant", "zebra"}, 
    "ZoneB": {"elephant", "tiger", "zebra"},
    "ZoneC": {"tiger", "giraffe"}
}

while True:
    print("\n1. Perform a set operation")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        operation = input("Enter the operation (union, intersection, difference): ")
        zone1 = input("Enter the first zone: ")
        zone2 = input("Enter the second zone (leave blank for union): ") or None
        perform_set_operation(zones, operation, zone1, zone2)
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please try again.")