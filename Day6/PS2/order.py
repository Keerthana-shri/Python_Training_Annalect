class Product:
    def __init__(self, product_id, name, price):
        '''Initialize product with its ID, name, and price'''
        self.product_id = product_id
        self.name = name
        self.price = price

class Order:
    '''Creating a class variable to keep track of order count'''
    order_count = 1 

    def __init__(self, products):
        '''Initialize order with a list of products'''
        self.order_id = Order.order_count
        '''Increment for the next order'''
        Order.order_count += 1  
        self.products = products
        self.total = self.calculate_total()  

    def calculate_total(self):
        '''Calculate the total price of all products in the order'''
        return sum(product.price for product in self.products)

class ProductCatalog:
    def __init__(self):
        '''Initialize an empty product catalog'''
        self.products = []

    def add_product(self, product_id, name, price):
        '''Add a new product to the catalog'''
        new_product = Product(product_id, name, price)
        self.products.append(new_product)

    def get_product_by_id(self, product_id):
        '''Retrieve a product from the catalog by its ID'''
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None