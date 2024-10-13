class circle:
    def __init__(self,r):
        self.r=r
    def display(self):
        print("area",3.14*self.r*self.r)
        print("perimeter",2*3.14*self.r) 
ob=circle(3)
ob.display()              
    