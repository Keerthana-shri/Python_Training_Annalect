class Product:
    def __init__(self, productid, productname, price):
        self.productid = productid
        self.productname = productname
        self.price = price

class Order:
    order_count = 1

    def __init__(self, products):
        self.order_id = Order.order_count
        Order.order_count += 1
        self.products = products
        self.total = self.calculate_total()

    def calculate_total(self):
        return sum(product.price for product in self.products)
