from product import Product
from db import Database

class Logic:
    def __init__(self):
        self.db = Database()

    def add_product(self, product_object):
        return self.db.add_product(product_object)

    def update_product(self, updated_product_object):
        return self.db.update_product(updated_product_object)

    def list_all(self):
        return self.db.list_all()

    def apply_discount(self, discount):
        return self.db.apply_discount(discount)


