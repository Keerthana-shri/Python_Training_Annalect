from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    productid = Column(Integer, primary_key=True)
    productname = Column(String, nullable=False)
    price = Column(Float, nullable=False)

class Database:
    def __init__(self, db_name="sqlite:///product_management.db"):
        """Initialize the database connection."""
        self.engine = create_engine(db_name)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def add_product(self, product):
        """Add a new product to the database."""
        self.session.add(product)
        self.session.commit()
        return True

    def update_product(self, updated_product):
        """Update an existing product's price."""
        product = self.session.query(Product).filter_by(productid=updated_product.productid).first()
        if product:
            product.price = updated_product.price
            self.session.commit()
            return True
        return False

    def list_all(self):
        """List all products in the database."""
        products = self.session.query(Product).all()
        if products:
            return products
        else:
            return False
        
    def apply_discount(self, discount):
        """Apply a discount to all products' prices."""
        products = self.session.query(Product).all()
        if products:
            for product in products:
                product.price -= product.price * discount / 100
            self.session.commit()
            return True
        return False

    def close(self):
        """Close the database connection."""
        self.session.close()