'''Importing necessary modules'''
from product import Product
import csv

class Logic:
    '''A class to represent the logic for the operations in product management system'''
    def __init__(self):
        '''Initialise by creating an empty list'''
        self.product=[]

    def write_products_to_csv(self, filename='products.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Write the header row
            writer.writerow(['productid', 'productname', 'price'])
            
            # Write each product as a row in the CSV
            for i in self.product:
                writer.writerow(i.to_csv_row())

    def read_products_from_csv(filename='products.csv'):
        products=[]
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            
            # Skip the header row
            next(reader)
            
            # Read each row and create a Product object
            for row in reader:
                product = Product.from_csv_row(row)
                products.append(product)
        
        return products

    def add_product(self,product_object):
        """Adds a product if it does not already exist based on product ID."""
        for i in self.product:
            if i.productid == product_object.productid:
                return False
        self.product.append(product_object)
        return True

    # def update_product(self, productid, productname, price):
    #     """Updates the product's name and price based on product ID."""
    #     for i in self.product:
    #         if i.productid == productid:
    #             i.productname = productname
    #             i.price = price
    #             return True
    #         else:
    #             return False

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