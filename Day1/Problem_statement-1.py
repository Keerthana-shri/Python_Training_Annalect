def product_management_system():
    products = {}

    def add_product(product_id, name, price):
        if product_id in products:
            print(f"Product with ID {product_id} already exists.")
        else:
            products[product_id] = {"name": name, "price": price}
            print(f"Product {name} added with ID {product_id}.")


    def list_products():
        if products:
            for product_id, details in products.items():
                print(f"ID: {product_id}, Name: {details['name']}, Price: ${details['price']}")
        else:
            print("No products available.")


    def update_product(product_id, name=None, price=None):
        if product_id in products:
            if name:
                products[product_id]["name"] = name
            if price:
                products[product_id]["price"] = price
            print(f"Product {product_id} updated.")
        else:
            print(f"Product with ID {product_id} does not exist.")


    def apply_discount(percentage):
        if products:
            print(f"Applying {percentage}% discount to all products.")
            for product_id in products:
                old_price = products[product_id]["price"]
                products[product_id]["price"] = round(old_price * (1 - percentage / 100), 2)
            print("Discount applied.")
        else:
            print("No products available to apply a discount.")

    
    while True:
        print("\nProduct Management System")
        print("1. Add Product")
        print("2. List Products")
        print("3. Update Product")
        print("4. Apply Discount")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            list_products()
        elif choice == '3':
            update_product()
        elif choice == '4':
            apply_discount()
        elif choice == '5':
            print("Exiting Product Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

product_management_system()