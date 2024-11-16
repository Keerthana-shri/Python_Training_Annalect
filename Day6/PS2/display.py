'''Importing necessary modules'''
from order import ProductCatalog
from logic import Logic

'''Initialize Product Catalog'''
catalog = ProductCatalog()

'''Adding products to the catalog'''
catalog.add_product(1, "Laptop", 1500.00)
catalog.add_product(2, "Mouse", 20.00)
catalog.add_product(3, "Keyboard", 30.00)

'''Initialize Logic instance'''
logic = Logic()

'''Order creation'''
print("Placing an order for a Laptop and Mouse...")
product_list = [catalog.get_product_by_id(1), catalog.get_product_by_id(2)]
order_id = logic.place_order(product_list)  
print(f"Order ID {order_id} placed successfully.")

'''Listing all orders'''
print("\nList of all orders:")
for order in logic.list_orders():  
    print(f"Order ID: {order[0]}, Products: {order[1]}, Total: Rs {order[2]:.2f}")

'''Calculating total cost of all orders'''
total_cost = logic.calculate_total_cost()  
print(f"\nTotal cost of all orders: Rs {total_cost:.2f}")

'''Canceling an order'''
print(f"\nCancelling order with ID {order_id}")
a= logic.cancel_order(order_id)  
print("Order cancelled.")

'''Listing all orders after cancellation'''
print("\nList of all orders after cancellation:")
for order in logic.list_orders(): 
    print(f"Order ID: {order[0]}, Products: {order[1]}, Total: Rs {order[2]:.2f}")

'''Summarizing all orders'''
b= logic.summarize_orders()

