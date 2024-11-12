from presentation import presentation
from logic import logic
from product import Product

def start():

    logic_object=logic()
    # presentation_object=presentation()

    from product import Product
    product_object = [
            Product(1, "Smartwatch", 1500),
            Product(2, "Headphone", 2000)
        ]

    for Product in product_object:
        a= logic_object.add_product(Product)
        if a == True:
             print("Added")
        else:
             print("Failed")
    
    b= logic_object.update_product(1, "Smartphone", 16000)
    if b == True:
        print ("Product is updated")
    else:
        print ("Product ID is not found")
    
    c= logic_object.list_all()
    print("All products are listed below:")
    for i in c:
        print(i)

    
if __name__ == "__main__":
    start()