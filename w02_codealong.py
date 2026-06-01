import math
#square
#Ask for the informmation
side = int(input("What is the lenght of a side of the square? "))

#calculate the the area 
square_area = side ** 2

#Display the value
print(f"The area of the square is: {square_area:.4f}")

#rectangle
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
# print(f"The area of the rectangle is {length * width}")

rectangle_area = length * width
print(f"The area of the rectangle is: {rectangle_area}")

#circle
radius = float(input(f"What is the radius of th circle? "))
circle_area = math.pi * radius ** 2
print(f"The area of the circle is {circle_area}")

### The following works with square cms

#square
#Ask for the informmation
side = float(input("What is the lenght of a side of the square (in cm)? "))

#calculate the the area 
square_area = side ** 2

#Display the value
print(f"The area of the square is: {square_area:.4f} cm^2")
area_meters = square_area / 10000
print(f"The area of the square is {area_meters:.4f} m^2")

#rectangle
length = float(input("What is the length of the rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
# print(f"The area of the rectangle is {length * width}")

rectangle_area = length * width
rectangle_area_meters = rectangle_area / 10000
print(f"The area of the rectangle is: {rectangle_area} in cm^2 or {rectangle_area_meters} m^2")

#circle
radius = float(input(f"What is the radius of th circle (in cm)? "))
circle_area = math.pi * radius ** 2
circle_area_meters = circle_area / 10000
print(f"The area of the circle is {circle_area} cm^2 or {circle_area_meters} m^2")