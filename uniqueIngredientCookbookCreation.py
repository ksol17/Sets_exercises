def display_unique_ingredients(recipes, filter_criteria=None):
    unique_ingredients = {ingredient for recipe in recipes for ingredient in recipe if not filter_criteria or ingredient in filter_criteria}
    print("Unique ingredients in Cookbook:")
    print(', '.join(unique_ingredients))


recipes = [
    {"chicken", "lemon", "garclic", "thyme"},
    {"salmon", "lemon", "dill"},
    {"eggplant", "garlic", "tomato", "basil"},
    {"beef", "onion", "garlic", "rosemary"}
]

vegetarian_ingredients = {"eggplant", "garlic", "tomato", "basil", "dill", "onoin"}

while True:
    print("\n1. Display all unique ingredients")
    print("2. Display unique vegetarian ingredients")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_unique_ingredients(recipes)
    elif choice == '2':
        display_unique_ingredients(recipes, vegetarian_ingredients)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")