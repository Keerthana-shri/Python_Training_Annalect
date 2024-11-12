from logic import logic

class presentation:
    while True:
        print("\nProduct Management System")
        print("1. Add Product")
        print("2. List Products")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            productid = input("Enter product ID: ")
            productname = input("Enter product name: ")
            price = input("Enter product price: ")
            a = add_product(productid, productname, price)
            print(a)
        elif choice == '2':
            d=list_products()
            print(d)
        elif choice == '5':
            print("Exiting Product Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
