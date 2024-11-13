class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Order:
    order_count = 1 

    def __init__(self, products):
        self.order_id = Order.order_count
        '''Increment for the next order'''
        Order.order_count += 1  
        self.products = products
        self.total = self.calculate_total()

    def calculate_total(self):
        return sum(product.price for product in self.products)

class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product_id, name, price):
        new_product = Product(product_id, name, price)
        self.products.append(new_product)

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
