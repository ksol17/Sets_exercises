def compare_routes(airlines, operation, airline1, airline2):
    routes1 = airlines.get(airline1, set())
    routes2 = airlines.get(airline2, set())

    if operation == 'issubset':
        result = routes1.issubset(routes2)
        print(result)
    elif operation == 'issuperset':
        result = routes1.issuperset(routes2)
        print(result)
    elif operation == 'isdisjoint':
        result = routes1.isdisjoint(routes2)
        print(result)
    else:
        print("Invalid operation.")
        return


airlines = {
    "AirlineA": {"LAX", "JFK", "CDG"},
    "AirlineB": {"LAX", "JFK", "CDG", "DXB"}, 
    "AirlineC": {"HND", "LHR", "SFO"}
}

while True:
    print("\n1. Compare flight routes")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        operation = input("Enter the operation(issubset, issuperset, isdisjoint): ")
        airline1 = input("Enter the first airline: ")
        airline2 = input("Enter the second airline: ")
        compare_routes(airlines, operation, airline1, airline2)
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please try again.")