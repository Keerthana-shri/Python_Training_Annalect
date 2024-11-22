from order import Product
from logic import Logic
from db import Database

# Initialize Logic instance
logic = Logic()

# Adding products to the database
products = [
    Product(1, "Laptop", 1500.00),
    Product(2, "Mouse", 20.00),
    Product(3, "Keyboard", 30.00),
    Product(4, "Monitor", 300.00),
    Product(5, "Printer", 120.00)
]

for product in products:
    logic.add_product(product)

# Place three orders
print("Placing an order for a Laptop and Mouse...")
product_list1 = [products[0], products[1]]
order_id1 = logic.place_order(product_list1)
print(f"Order ID {order_id1} placed successfully.")

print("Placing an order for a Keyboard and Monitor...")
product_list2 = [products[2], products[3]]
order_id2 = logic.place_order(product_list2)
print(f"Order ID {order_id2} placed successfully.")

print("Placing an order for a Printer...")
product_list3 = [products[4]]
order_id3 = logic.place_order(product_list3)
print(f"Order ID {order_id3} placed successfully.")

# List all orders
print("\nList of all orders:")
for order in logic.list_orders():
    print(f"Order ID: {order[0]}, Products: {order[1]}, Total: Rs {order[2]:.2f}")

# Calculate total cost of all orders
total_cost = logic.calculate_total_cost()
print(f"\nTotal cost of all orders: Rs {total_cost:.2f}")

# Cancel one order
print(f"\nCancelling order with ID {order_id2}")
logic.cancel_order(order_id2)
print("Order cancelled.")

# List all orders after cancellation
print("\nList of all orders after cancellation:")
for order in logic.list_orders():
    print(f"Order ID: {order[0]}, Products: {order[1]}, Total: Rs {order[2]:.2f}")

# Summarize all orders
logic.summarize_orders()
