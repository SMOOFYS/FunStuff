  
greeting = """
    Welcome to the Python Geometry Assistant!
              Let's do some math!
"""
print(greeting)

#circle circ = r2pi and circle area = rrpi
#triangle area = BH/2 triangle circ = base + height + hypotenuse

pi = 3.14
radius = float(input("Let's start with calculating the area and circumference of a circle! What is the radius of your circle?\n-> "))

circum = radius*pi*2
area = pi*radius ^ 2

print(f"Circle circumference: {circum}\nCircle area: {area}")

leg1 = float(input("Now let's calculate the perimeter and area of a triangle! What is the length of the leg of a triangle?\n-> "))
leg2 = float(input("What is the length of the other leg?\n-> "))
Side1 = float(input("What is the length of the last side?\n-> "))

perimeter = leg1 + leg2 + Side1
area2 = (leg1*leg2)/2

print(f"Triangle perimeter: {perimeter}\nTriangle area: {area2}")

square1 = float(input("Now let's calculate the area and perimeter of a square! What is the length of one side of the square?\n-> "))

square_perm = square1*4
square_area = square1 ^ 2

print(f"Square perimeter: {square_perm}\nSquare area: {square_area}")

rectangle1 = float(input("And finally, let's calculate the area and perimeter of a rectangle. What is the length of the rectangle?\n-> "))
rectangle2 = float(input("And what is the width of the rectangle?\n-> "))

rec_perm = rectangle1*2 + rectangle2*2
rec_area = rectangle1*rectangle2

print(f"Rectangle perimeter: {rec_perm}\nRectangle area: {rec_area}")