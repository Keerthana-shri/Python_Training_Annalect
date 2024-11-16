'''Importing necessary modules'''
import csv
from order import Product, Order, ProductCatalog

class Logic:
    '''Creating a class for defining functions for performing operations like place_order, list_order,
    calculate_total_cost, cancel_order, write_orders_to_csv, read_orders_from_csv'''
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

    def write_orders_to_csv(self, filename='orders.csv'):
        """Writes the list of orders to a CSV file."""
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['order_id', 'product_id', 'product_name', 'product_price', 'total'])
                for order in self.orders:
                    for product in order.products:
                        writer.writerow([order.order_id, product.product_id, product.name, product.price, order.total])
            return True
        except Exception as e:
            print(f"Error writing to CSV: {e}")
            return False

    def read_orders_from_csv(self, filename='orders.csv'):
        """Reads orders from a CSV file and returns a list of order objects."""
        orders = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                current_order_id = None
                current_order_products = []
                for row in reader:
                    order_id, product_id, product_name, product_price, total = row
                    product = Product.from_csv_row([product_id, product_name, product_price])
                    if current_order_id is None:
                        current_order_id = int(order_id)
                    if current_order_id != int(order_id):
                        orders.append(Order(current_order_products))
                        current_order_products = []
                        current_order_id = int(order_id)
                    current_order_products.append(product)
                if current_order_products:
                    orders.append(Order(current_order_products))
        except Exception as e:
            print(f"Error reading from CSV: {e}")
        self.orders = orders
        return orders