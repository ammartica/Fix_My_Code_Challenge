#!/usr/bin/python3
"""class that defines Square object"""


class Square():
    """Square object"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes Square object by setting values"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Returns perimeter of Square object """
        return 2 * (self.width + self.height)

    def __str__(self):
        """ String representation of Square object """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ creates a Square object and calls methods """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
