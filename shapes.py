
class Shape:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"This is a {self.name}.")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def display_info(self):
        super().display_info()
        print(f"It has a radius of {self.radius} units.")
        

class Square(Shape):
    def __init__(self, side_length):
        super().__init__("Square")
        self.side_length = side_length

    def display_info(self):
        super().display_info()
        print(f"It has a side length of {self.side_length} units.")

if __name__ == "__main__":
    circle = Circle(5)
    square = Square(4)

    circle.display_info()
    print()  
    square.display_info()

