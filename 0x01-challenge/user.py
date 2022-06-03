#!/usr/bin/python3
"""
User class
"""


class User():
    """ Create an object named User """

    def __init__(self):
        """ initialize User object attributes """
        self.__email = None

    @property
    def email(self):
        """getter for private instance attribute email"""
        return self.__email

    @email.setter
    def email(self, value):
        """ setter for User's email """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
