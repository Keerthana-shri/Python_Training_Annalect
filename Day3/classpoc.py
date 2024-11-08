class rect:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        area=self.length*self.breadth
    
    def perimeter(self):
        perimeter= 2(self.length+self.breadth)
    

r= rect(2,3)
r1=rect(7,9)
print(r.area)
print(r1.area)


print("hello")