#!/usr/bin/python3
""" Module creates a Square """


class Square:
    """
    Square class
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initializes Square object values """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Returns area of the Square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Returns permiter of a Square object"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of a Square object """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Calls Square class and methods """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
