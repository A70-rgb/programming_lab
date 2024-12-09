class Rectangle:
    def __init__(self, l, b):
        self._l1 = l
        self._b1 = b
        
    def area(self):
        return self._l1 * self._b1
    
    def __lt__(self,obj):
        if self.area() < obj.area():
            return "the area of rectangle1 is less than rectangle2"
        else:
            return "the area of the rectangle2 is less than rectangle1"
        
        
print("RECTANGLE 1")
l=int(input("enter the length of rectangle 1:"))
b=int(input("enter the breadth of rectangle 1:"))
obj1 = Rectangle( l , b )
print("the area of rectangle 1 is :", obj1.area())

print("RECTANGLE 2")
l=int(input("enter the length of rectangle 2:"))
b=int(input("enter the breadth of rectangle 2:"))
obj2 = Rectangle( l , b )

print("area of rectangle 1 is:", obj2.area())
print("\nNow comparing the rectangles")
print( obj1 < obj2 )