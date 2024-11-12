from product import Product

class logic:
    def __init__(self):
        self.product=[]

    def add_product(self,product_object):
        for i in self.product:
            if i.productid == product_object.productid:
                return False
        self.product.append(product_object)
        return True
    
    def update_product(self, productid, productname, price):
        for i in self.product:
            if i.productid == productid:
                i.productname = productname
                i.price = price
                return True
            else:
                return False
    
    def list_all(self):
        return self.product
    
    def apply_discount(self, discount):
        for i in self.product:
            i.price = i.price - (i.price * discount/100)
        return False