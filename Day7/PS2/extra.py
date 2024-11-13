
# def cancel_order(order_id):
#     """Cancels an order by removing it from the orders list."""
#     global orders
#     orders = [order for order in orders if order.order_id != order_id]

# '''Canceling an order'''
# print(f"\nCancelling order with ID {order_id}")
# cancel_order(order_id)
# print("Order cancelled.")

# '''Listing all orders after cancellation'''
# print("\nList of all orders after cancellation:")
# for order in list_orders():
#     print(f"Order ID: {order[0]}, Products: {order[1]}, Total: Rs {order[2]:.2f}")