class Product:

    def __init__(self,productid,productname,price):
        '''Inizialise product with its parameters'''
        self.productid=productid
        self.productname=productname
        self.price=price
    
    def __str__(self):
        '''Returns a formatted string with the product's ID, name, and price.'''
        return f"ProductID: {self.productid} - ProductName: {self.productname} - Price: {self.price}"