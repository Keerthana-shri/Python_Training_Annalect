'''Importing necessary modules'''
from product import Product


class Logic:
    '''A class to represent the logic for the operations in product management system'''
    def __init__(self):
        '''Initialise by creating an empty list'''
        self.product=[]

    def add_product(self,product_object):
        """Adds a product if it does not already exist based on product ID."""
        for i in self.product:
            if i.productid == product_object.productid:
                return False
        self.product.append(product_object)
        return True

    def update_product(self, updated_product_object):
        """Updates the product's name and price based on product ID."""
        for i in self.product:
            if i.productid == updated_product_object.productid:
                i.price = updated_product_object.price
                return True
        return False

    def list_all(self):
        """Returns a list of all products."""
        return self.product
    
    def apply_discount(self, discount):
        """Applies a discount to all products' prices."""
        discount_applied= False
        for i in self.product:
            i.price = i.price - (i.price * discount/100)
            discount_applied = True
        return discount_applied