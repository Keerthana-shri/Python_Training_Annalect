'''Importing necessary modules'''
from order import ProductCatalog
from logic import Logic

def main():
    '''Initialize Product Catalog'''
    catalog = ProductCatalog()

    '''Adding products to the catalog'''
    catalog.add_product(1, "Laptop", 1500.00)
    catalog.add_product(2, "Mouse", 20.00)
    catalog.add_product(3, "Keyboard", 30.00)
    catalog.add_product(4, "Monitor", 300.00)

    '''Initialize Logic instance'''
    logic = Logic()

    '''Order creation'''
    print("Placing an order for a Laptop and Mouse...")
    product_list1 = [catalog.get_product_by_id(1), catalog.get_product_by_id(2)]
    order_id1 = logic.place_order(product_list1)
    print(f"Order ID {order_id1} placed successfully.")

    print("Placing an order for a Keyboard and Monitor...")
    product_list2 = [catalog.get_product_by_id(3), catalog.get_product_by_id(4)]
    order_id2 = logic.place_order(product_list2)
    print(f"Order ID {order_id2} placed successfully.")

    '''Listing all orders'''
    print("\nList of all orders:")
    for order in logic.list_orders():
        print(f"Order ID: {order[0]}, Products: {order[1]}, Total: Rs {order[2]:.2f}")

    '''Calculating total cost of all orders'''
    total_cost = logic.calculate_total_cost()
    print(f"\nTotal cost of all orders: Rs {total_cost:.2f}")

    '''Canceling an order'''
    print(f"\nCancelling order with ID {order_id1}")
    logic.cancel_order(order_id1)
    print("Order cancelled.")

    '''Listing all orders after cancellation'''
    print("\nList of all orders after cancellation:")
    for order in logic.list_orders():
        print(f"Order ID: {order[0]}, Products: {order[1]}, Total: Rs {order[2]:.2f}")

    '''Summarizing all orders'''
    logic.summarize_orders()

    '''Write orders to CSV'''
    if logic.write_orders_to_csv():
        print("\nOrders written to CSV successfully.")

    '''Read orders from CSV'''
    print("\nReading orders from CSV...")
    orders_from_csv = logic.read_orders_from_csv()
    print("Read orders from CSV:")
    for order in orders_from_csv:
        print(f"Order ID: {order.order_id}, Products: {[(p.name, p.price) for p in order.products]}, Total: Rs {order.total:.2f}")

if __name__ == "__main__":
    main()