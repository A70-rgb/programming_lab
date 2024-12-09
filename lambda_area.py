x=int(input("enter the side of square:"))
area=lambda x:x*x
print("Area of square :{0}".format(area(x)))
l=int(input("enter the length of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))
area=lambda l,b:l*b
print("Area of the triangle:{0}".format(area(l,b)))
b=int(input("enter the breadth of the triangle"))
h=int(input("enter the height of the triangle"))
area=lambda b,h:0.5*b*h
print("Area of the triangle :{0}".format(area(b,h)))