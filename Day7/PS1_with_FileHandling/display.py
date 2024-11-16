'''Importing necessary modules'''
from logic import Logic
from product import Product
from update_product import UpdateProduct

def start():
    '''Initializing product management system operations - add, update, listing products and applying discounts. 
    It Demonstrates interactions between the Logic and Product classes.'''

    logic_object = Logic()
    
    product_objects = [
        Product(1, "Smartwatch", 1500),
        Product(2, "Headphone", 2000)
    ]

    '''Add products to the Logic instance'''
    for product in product_objects:
        if logic_object.add_product(product):
            print("Added")
        else:
            print("Failed")
    
    '''Update the information of a product'''
    updated_product_object = UpdateProduct(1, 5000)
    if logic_object.update_product(updated_product_object):
        print("Product is updated")
    else:
        print("Product ID is not found")
    
    '''Apply discount to the product's price'''
    if logic_object.apply_discount(50):
        print("Discount is applied")

    '''List all the products'''
    products = logic_object.list_all()
    print("All products are listed below:")
    for product in products:
        print(product)
    
    '''Write products to CSV'''
    if logic_object.write_products_to_csv():
        print("Written successfully")
    
    '''Read products from CSV'''
    read_products = logic_object.read_products_from_csv()
    print("Read products from CSV:")
    for product in read_products:
        print(product)


if __name__ == "__main__":
    '''Calling the function'''
    start()
