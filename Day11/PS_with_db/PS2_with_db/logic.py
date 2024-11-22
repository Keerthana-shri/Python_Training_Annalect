from db import Database
from order import Order
from order import Product

class Logic:
    def __init__(self):
        self.db = Database()
        self.db.create_table()

    def add_product(self, product_object):
        return self.db.add_product(product_object)

    def update_product(self, updated_product_object):
        return self.db.update_product(updated_product_object)

    def list_all(self):
        return self.db.list_all()

    def apply_discount(self, discount):
        return self.db.apply_discount(discount)

    def place_order(self, products):
        """Places a new order with a list of products and adds it to the orders list."""
        new_order = Order(products)
        self.db.place_order(new_order)
        return new_order.order_id

    def list_orders(self):
        """Returns a list of all orders with details."""
        orders = self.db.list_orders()
        return [(order[0], order[1].split(','), order[2]) for order in orders]

    def calculate_total_cost(self):
        """Calculates the total cost of all orders."""
        orders = self.db.list_orders()
        return sum(order[2] for order in orders)

    def cancel_order(self, order_id):
        """Cancels an order by removing it from the orders list."""
        return self.db.delete_order(order_id)

    def summarize_orders(self):
        """Prints a summary of all orders."""
        total_orders = len(self.db.list_orders())
        total_cost = self.calculate_total_cost()
        print(f"\nSummary of all orders:")
        print(f"Total number of orders: {total_orders}")
        print(f"Total cost of all orders: Rs {total_cost:.2f}")
        for order in self.db.list_orders():
            print(f"Order ID: {order[0]}, Total: Rs {order[2]:.2f}")
