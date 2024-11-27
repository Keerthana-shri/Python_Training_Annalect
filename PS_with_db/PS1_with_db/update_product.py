class UpdateProduct:

    def __init__(self,productid, price):
        '''Initialize product with its parameters for updating'''
        self.productid=productid
        self.price=price
    
    def __str__(self):
        '''Returns a formatted string with the product's ID and updated price.'''
        return f"ProductID: {self.productid} - Price: {self.price}" 
