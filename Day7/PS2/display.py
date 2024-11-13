'''Importing necessary modules'''
from order import ProductCatalog
from logic import Logic

catalog = ProductCatalog()

'''Adding products to the catalog'''
catalog.add_product(1, "Laptop", 1500.00)
catalog.add_product(2, "Mouse", 200.00)
catalog.add_product(3, "Keyboard", 900.00)

'''Placing an order'''
print("Placing an order")
product_list = [catalog.get_product_by_id(1), catalog.get_product_by_id(2)]
order_id = Logic.place_order(product_list)
print(f"Order ID {order_id} placed successfully.")

'''Listing all orders'''
print("\nList of all orders:")
for order in Logic.list_orders():
    print(f"Order ID: {order[0]}, Products: {order[1]}, Total: Rs {order[2]:.2f}")

'''Calculating total cost of all orders'''
total_cost = Logic.calculate_total_cost()
print(f"\nTotal cost of all orders: Rs {total_cost:.2f}")

