'''Importing necessary modules'''
from PS1_logic import Logic
from PS1_db_sqlalchemy import Product as DBProduct  # Rename the imported Product class
from PS1_update_product import UpdateProduct

def start():
    '''Initializing product management system operations - add, update, listing products and applying discounts. 
    It Demonstrates interactions between the Logic and Product classes.'''

    logic_object = Logic()
    
    product_object = [
        DBProduct(productid=1, productname="Smartwatch", price=1500),
        DBProduct(productid=2, productname="Headphone", price=2000)
    ]

    '''Add products to the Logic instance'''
    for product in product_object:
        existing_product = logic_object.db.session.query(DBProduct).filter_by(productid=product.productid).first()
        if existing_product:
            print(f"Product with ID {product.productid} already exists. Skipping addition.")
        else:
            a = logic_object.add_product(product)
            if a:
                print("Added")
            else:
                print("Failed")
    
    '''Update the information of a product'''
    updated_product_object = UpdateProduct(1, 5000)
    b = logic_object.update_product(updated_product_object)
    if b:
        print("Product is updated")
    else:
        print("Product ID is not found")
    
    '''Apply discount to the product's price'''
    d = logic_object.apply_discount(50)
    if d:
        print("Discount is applied")
    else:
        print("Failed to apply discount")

    '''List all the products'''
    c = logic_object.list_all()
    if c:
        print("All products are listed below:")
        for i in c:
            print(f"ProductID: {i.productid} - ProductName: {i.productname} - Price: {i.price}")
    else:
        print("No products found")
    

if __name__ == "__main__":
    '''Calling the function'''
    start()