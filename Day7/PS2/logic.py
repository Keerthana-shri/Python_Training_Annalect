'''Importing necessary modules'''
from order import Product, Order, ProductCatalog

class Logic:
    '''Create empty list for storing all the orders'''
    orders = []

    def place_order(products):
        """Places a new order with a list of products and adds it to the orders list."""
        new_order = Order(products)
        Logic.orders.append(new_order)
        return new_order.order_id

    def list_orders():
        """Returns a list of all orders with details."""
        return [(order.order_id, [(p.name, p.price) for p in order.products], order.total) for order in Logic.orders]

    def calculate_total_cost():
        """Calculates the total cost of all orders."""
        return sum(order.total for order in Logic.orders)


