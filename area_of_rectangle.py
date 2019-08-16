class rectangle:
    def __init__(self,height,width):
        self.x=height
        self.y=width
    def method(self):
        area=self.x*self.y
        print(area)
h=int(input("enter the number : "))
w=int(input("enter the number : "))
ob=rectangle(h,w)
ob.method()


