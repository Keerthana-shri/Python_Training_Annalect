import sqlite3

class Database:
    def __init__(self, db_name="order_management.db"):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create the products and orders tables if they don't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                productid INTEGER PRIMARY KEY,
                productname TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                product_ids TEXT NOT NULL,
                total REAL NOT NULL
            )
        ''')
        self.connection.commit()

    def add_product(self, product):
        """Add a new product to the database."""
        try:
            self.cursor.execute('''
                INSERT INTO products (productid, productname, price)
                VALUES (:productid, :productname, :price)
            ''', {'productid': product.productid, 'productname': product.productname, 'price': product.price})
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def update_product(self, updated_product):
        """Update an existing product's price."""
        self.cursor.execute('''
            UPDATE products
            SET price = :price
            WHERE productid = :productid
        ''', {'price': updated_product.price, 'productid': updated_product.productid})
        self.connection.commit()
        return self.cursor.rowcount > 0

    def list_all(self):
        """List all products in the database."""
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def apply_discount(self, discount):
        """Apply a discount to all products' prices."""
        self.cursor.execute('''
            UPDATE products
            SET price = price - (price * :discount / 100)
        ''', {'discount': discount})
        self.connection.commit()
        return self.cursor.rowcount > 0

    def place_order(self, order):
        """Place a new order in the database."""
        product_ids = ','.join(str(p.productid) for p in order.products)
        self.cursor.execute('''
            INSERT INTO orders (order_id, product_ids, total)
            VALUES (:order_id, :product_ids, :total)
        ''', {'order_id': order.order_id, 'product_ids': product_ids, 'total': order.total})
        self.connection.commit()
        return order.order_id

    def list_orders(self):
        """List all orders from the database."""
        self.cursor.execute('SELECT * FROM orders')
        return self.cursor.fetchall()

    def delete_order(self, order_id):
        """Delete an order from the database."""
        self.cursor.execute('DELETE FROM orders WHERE order_id = :order_id', {'order_id': order_id})
        self.connection.commit()
        return self.cursor.rowcount > 0

    def close(self):
        """Close the database connection."""
        self.connection.close()

