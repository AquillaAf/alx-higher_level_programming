#!/usr/bin/python3
from models.base import Base
""" module creates a Rectangle class"""
class Rectangle(Base):
    """
    A rectangle class is created in heriting from base.
    Attributes:
        width (int): the  width of the rectangle
        height (int): the height of the rectangle
        x (int):
        y (int):
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError ("width must be an integer")
        if value <= 0:
            raise ValueError ("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,value):
        if not isinstance(value, int):
            raise TypeError ("height must be an integer")
        if value <= 0:
            raise ValueError ("height must be > 0")
        self.__height = value


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError ("x must be an integer")
        if value < 0:
            raise ValueError ("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError ("y must be an integer")
        if value < 0:
            raise ValueError ("y must be >= 0")
        self.__y = value


    def area (self):
        return (self.width * self.height)


    def display(self):
        for item in range(self.height):
            for row in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, 
                                                self.x, 
                                                self.y, 
                                                self.width, 
                                                self.height)
    def update(self, *args, **kwargs):
        
        if not args and len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
        else:
            a = 0
            for item in args:
                if a == 0:
                    self.id = item
                elif a == 1:
                    self.width = item
                elif a == 2:
                    self.height = item
                elif a == 3:
                    self.x = item
                elif a == 4:
                    self.y = item
                a += 1

    def to_dictionary(self):
        return {'id' : self.id,
                'width' : self.width,
                'x' : self.x,
                'y' : self.y
                }
