class Product:
    def __init__(self, productid, productname, price):
        '''Initialize product with its parameters'''
        self.productid = productid
        self.productname = productname
        self.price = price
    
    def __str__(self):
        '''Returns a formatted string with the product's ID, name, and price.'''
        return f"ProductID: {self.productid} - ProductName: {self.productname} - Price: {self.price}"
    
    def to_csv_row(self):
        '''Converts the product object to a list for CSV writing'''
        return [self.productid, self.productname, self.price]

    @classmethod
    def from_csv_row(cls, row):
        '''Creates a product object from a CSV row'''
        productid, productname, price = row
        return cls(int(productid), productname, float(price))