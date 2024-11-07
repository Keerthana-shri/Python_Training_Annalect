'''Problem Statement 1: Product Management System
Objective: Create a system to manage products in a manufacturing company.

Requirements:

Implement functions to
 add new products,
  list existing products, 
  and update product information 
(e.g., price).

Each product should have a unique identifier, name, and price.
Create a function to apply discounts to all products based on a percentage.
Ensure that you can handle edge cases, such as trying to update a product that doesn't exist.'''

def product_management_system():
    products = {}

    def add_product(product_id, name, price):
        if product_id in products:
            return(f"Product with ID {product_id} already exists.")
        else:
            products[product_id] = {"name": name, "price": price}
            return(f"Product {name} added with ID {product_id}.")


    def list_products():
        if products:
            for product_id, details in products.items():
                return(f"ID: {product_id}, Name: {details['name']}, Price: ${details['price']}")
        else:
            return("No products available.")

    
    while True:
        print("\nProduct Management System")
        print("1. Add Product")
        print("2. List Products")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            a = add_product(product_id, name, price)
            print(a)
        elif choice == '2':
            d=list_products()
            print(d)
        elif choice == '5':
            print("Exiting Product Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

product_management_system()