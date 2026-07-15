class Rectangle(object):
    """ Rectangle class """
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def __str__(self):
        rec_string = ""
        for n in range(self.height):
            rec_string += self.width * "#"
            rec_string += "\n"
        return rec_string
    
    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height
    
    def perimeter(self):
        """returns the perimeter of the rectangle"""
        return 2 * self.width + 2* self.height
    
    
recker = Rectangle(20, 5)
print(recker)