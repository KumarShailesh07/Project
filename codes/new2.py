class product:
    deliveryCharge=50
    def __init__(self,nam="Teddy Bear", prc=500):
        self.name=nam
        self.price=prc
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price + product.deliveryCharge
    def __str__(self):
        return "The {} will cost you Rs.{}.".format(self.get_name(),self.get_price())
    
class gift(product):
    def __init__(self,nam,prc,wrp):
        super().__init__(nam,prc)
        self.wrapping=wrp
    def get_price(self):
        return self.price+product.deliveryCharge+self.wrapping
    
p1=print(product())