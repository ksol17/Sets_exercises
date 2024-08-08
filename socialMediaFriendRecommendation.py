def get_friend_recommendations(users, user_name):
    if user_name not in users:
        print("User not found")
        return
    
    potential_friends = set()

    for friend in users[user_name]:
        potential_friends.update(users[friend])

    potential_friends.difference_update(users[user_name])
    potential_friends.discard(user_name)

    print(f"Friend recommendations for {user_name}: {', '.join(potential_friends)}")

try:
    num_users = int(input("Enter the number of users: "))
    users = {}

    for _ in range(num_users):
        name = input("Enter your name: ")
        friends = set(input("Enter friends (comma-separated): ").split(','))
        users[name] =friends


    user_name = input("Enter the name of the user to get friend recommendations: ")
    get_friend_recommendations(users, user_name)
except:
    pass