'''Importing necessary modules'''
import csv
from product import Product

class Logic:
    '''A class to represent the logic for the operations in product management system'''
    def __init__(self):
        '''Initialise by creating an empty list'''
        self.product = []

    def write_products_to_csv(self, filename='products.csv'):
        '''Writes the list of products to a CSV file'''
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['productid', 'productname', 'price'])  # Write the header row
                for product in self.product:
                    writer.writerow(product.to_csv_row())  # Write each product's data
            return True
        except Exception as e:
            print(f"Error writing to CSV: {e}")
            return False

    def read_products_from_csv(self, filename='products.csv'):
        '''Reads products from a CSV file and returns a list of product objects'''
        products = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    product = Product.from_csv_row(row)  # Create a product object from each row
                    products.append(product)
        except Exception as e:
            print(f"Error reading from CSV: {e}")
        return products

    def add_product(self, product_object):
        '''Adds a product if it does not already exist based on product ID.'''
        if any(product.productid == product_object.productid for product in self.product):
            return False 
        self.product.append(product_object)
        return True

    def update_product(self, updated_product_object):
        '''Updates the product's price based on product ID.'''
        for product in self.product:
            if product.productid == updated_product_object.productid:
                product.price = updated_product_object.price 
                return True
        return False 

    def list_all(self):
        '''Returns a list of all products.'''
        return self.product
    
    def apply_discount(self, discount):
        '''Applies a discount to all products' prices.'''
        for product in self.product:
            product.price -= product.price * discount / 100 
        return True