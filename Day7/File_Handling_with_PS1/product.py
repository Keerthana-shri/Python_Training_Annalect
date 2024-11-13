class Product:

    def __init__(self,productid,productname,price):
        '''Inizialise product with its parameters'''
        self.productid=productid
        self.productname=productname
        self.price=price
    
    def __str__(self):
        '''Returns a formatted string with the product's ID, name, and price.'''
        return f"ProductID: {self.productid} - ProductName: {self.productname} - Price: {self.price}"
    
    def to_csv_row(self):
        return [self.productid, self.productname, self.price]

    # Class method to create a Product from a CSV row (to read from CSV)
    @classmethod
    def from_csv_row(cls, row):
        productid, productname, price = row
        return cls(int(productid), productname, float(price))