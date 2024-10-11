# Creating python class rectangle
class rectangle:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def area (self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 *(self.width + self.height) 
    # now we interact with the user
# if __name__ == "__main__":
# the input from the user we get
width = input("Enter the width of the rectangle: ")
height = input("Enter the height of the rectangle: ")
Rectangle = rectangle(width, height)
print(f"Area: {Rectangle.area()}")
print(f"Perimeter: {Rectangle.perimeter()}")
# we can get input now from the userS