shape_list = ["1. Square", "2. Triangle", "3. Circle", "4. Rectangle"]
print("Select shape: ", shape_list)
shape = input()
print("Select unit: ")
unit = input()

if shape == "Square":
    squareWidth = float(input("Enter width: "))
    squareArea = squareWidth ** 2
    print("The area of square is ", squareArea, unit, "²")
elif shape == "Triangle":
    TriBase = float(input("Enter base: "))
    TriHeight = float(input("Enter Height: "))
    TriangleArea = 1/2 * (TriBase * TriHeight)
    print("The area of the Triangle is: ", TriangleArea, unit, "²")
elif shape == "Circle":
    CircleRadius = float(input('Enter Radius: '))
    CircleArea = 3.14 * (CircleRadius ** 2)
    print("The area of the Circle is: ", CircleArea, unit, "²")
elif shape == "Rectangle":
    RectangleLength = float(input("Enter length: "))
    RectangleWidth = float(input("Enter Width: "))
    RectangleArea = RectangleWidth * RectangleLength
    print("The area of the Rectangle is: ", RectangleArea, unit, "²")
else:
    print("Please select within the choices of shapes only.")