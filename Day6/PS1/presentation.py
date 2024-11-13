from logic import Logic

class Presentation:
    pass
    '''
    while True:
        print("\nProduct Management System")
        print("1. Add Product")
        print("2. List Products")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        w = logic()

        if choice == '1':
            productid = input("Enter product ID: ")
            productname = input("Enter product name: ")
            price = input("Enter product price: ")
            a = w.add_product(productid, productname, price)
            print(a)
        elif choice == '2':
            b=w.list_all()
        elif choice == '3':
            productid = input("Enter product ID: ")
            c = w.update_product(productid, productname, price)
            print(c)
        elif choice == '5':
            print("Exiting Product Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
    '''
