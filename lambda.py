area_square=lambda side:side**2
area_rectangle=lambda length,width:length*width
area_triangle=lambda base,height:0.5*base*height
side=float(input("Enter the side of the length of the square:"))
print("Area of the square:",area_square(side))
length=float(input("enter the length of the rectangle:"))
width=float(input("enter the width of the rectangle:"))
print("Area of rectangle:",area_rectangle(length,width))
base=float(input("Enter the base length of the triangle:"))
height=float(input("enter the height of the triangle:"))
print("Area of triangle:",area_triangle(base,height))

