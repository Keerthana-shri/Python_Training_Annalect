import sqlite3

class Database:
    def __init__(self, db_name="product_management.db"):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create the products table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                productid INTEGER PRIMARY KEY,
                productname TEXT NOT NULL,
                price REAL NOT NULL
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

    def close(self):
        """Close the database connection."""
        self.connection.close()
