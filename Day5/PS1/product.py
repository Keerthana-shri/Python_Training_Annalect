class Product:

    def __init__(self,productid,productname,price):
        self.productid=productid
        self.productname=productname
        self.price=price

    
    def __str__(self):
        return f"ProductID: {self.productid} - ProductName: {self.productname} - Price: {self.price}"