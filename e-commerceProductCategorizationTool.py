def categorize_products(num_products):
    product_categories = set()

    for _ in range(num_products):
        try:
            product_input = input("Enter product and category: ")
            product, category = product_input.split(',')
            product_categories.add((product.strip(), category.strip()))
        except ValueError:
            print("Invalid input. Please enter in the format 'product, category'.")

        print(product_categories)
        categorized = {}
        for product, category in product_categories:
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(product)
        
        for category, products in categorized.items():
            print(f"Category: {category}")
            for product in products:
                print(f" - {product}")


try:
    num_products = int(input("Enter the number of products: "))
    categorize_products(num_products)
except ValueError:
    print("Please enter a valid integer for the number of products. ")