'''Importing necessary modules'''
from order import Product, Order, ProductCatalog

class Logic:
    '''Creating a class for defining functions for performing operations like place_order, list_order,
    calculate_total_cost, cancle_order'''
    def __init__(self):
        self.orders = []  

    def place_order(self, products):
        """Places a new order with a list of products and adds it to the orders list."""
        new_order = Order(products)
        self.orders.append(new_order)  
        return new_order.order_id

    def list_orders(self):
        """Returns a list of all orders with details."""
        return [(order.order_id, [(p.name, p.price) for p in order.products], order.total) for order in self.orders]

    def calculate_total_cost(self):
        """Calculates the total cost of all orders."""
        return sum(order.total for order in self.orders)

    def cancel_order(self, order_id):
        """Cancels an order by removing it from the orders list."""
        self.orders = [order for order in self.orders if order.order_id != order_id]  

    def summarize_orders(self):
        """Prints a summary of all orders."""
        total_orders = len(self.orders)
        total_cost = self.calculate_total_cost()
        print(f"\nSummary of all orders:")
        print(f"Total number of orders: {total_orders}")
        print(f"Total cost of all orders: Rs {total_cost:.2f}")
        for order in self.orders:
            print(f"Order ID: {order.order_id}, Total: Rs {order.total:.2f}")

