class Product:
    def __init__(self, productid, productname, price):
        self.productid = productid
        self.productname = productname
        self.price = price

class Order:
    order_counter = 1

    def __init__(self, products):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.products = products
        self.total = sum(product.price for product in products)