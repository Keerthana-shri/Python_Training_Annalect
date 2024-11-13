from presentation import Presentation
from logic import Logic
import product
from update_product import UpdateProduct

def start():
    '''Initializing product management system operations - add, update, listing products and applying discounts. 
    It Demonstrates interactions between the Logic and Product classes.'''

    logic_object=Logic()
    #presentation_object=Presentation()
    
    product_object = [
            product.Product(1, "Smartwatch", 1500),
            product.Product(2, "Headphone", 2000)
        ]

    '''Add products to the Logic instance'''
    for product.Product in product_object:
        a= logic_object.add_product(product.Product)
        if a == True:
             print("Added")
        else:
             print("Failed")
    
    '''Update the information of a product'''
    updated_product_object = UpdateProduct(1, 5000)
    b= logic_object.update_product(updated_product_object)
    if b == True:
        print ("Product is updated")
    else:
        print ("Product ID is not found")

    # '''Update the information of a product'''
    # b= logic_object.update_product(1, "Smartphone", 16000)
    # if b == True:
    #     print ("Product is updated")
    # else:
    #     print ("Product ID is not found")
    
    '''Apply discount to the product's price'''
    d= logic_object.apply_discount(50)
    print("Discount is applied")

    '''List all the products'''
    c= logic_object.list_all()
    print("All products are listed below:")
    for i in c:
        print(i)
    

if __name__ == "__main__":
    '''Calling the function'''
    start()