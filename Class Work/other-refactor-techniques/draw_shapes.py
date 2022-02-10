# by Kami Bigdely
# Extract superclass.

class Shape:
    def __init__(self, x, y, visible, name):
        self.x = x
        self.y = y
        self.visible = visible
        self.name = name

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True

    def display(self):
        if self.visible:
            print(f"drew the {self.name}.")

    def get_center(self):
        return self.x, self.y


class Circle(Shape):
    def __init__(self, x, y, r, visible=True, name="circle"):
        super().__init__(x, y, visible, name)
        self.r = r


class Rectangle(Shape):
    def __init__(self, x, y, width, height, visible=True, name="rectangle"):
        super().__init__(x, y, visible, name)
        self.width = width
        self.height = height

    def get_center(self):
        return self.x + self.width / 2, self.y + self.height / 2


if __name__ == "__main__":
    circle = Circle(0, 0, 10, False)
    circle.show()
    circle.display()
    print('center point', circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display()  # does not display because it's hidden.
    rect.show()
    rect.display()
    print('center point', rect.get_center())
