import cv2

from square.Point import Point
from square.Square import Square


class Node:

    def __init__(self, square):
        self.square = square
        self.center = square.center
        self.marked = False
        self.children = []

    def mark(self, img):
        roi = img[int(self.square.get_top_left().y):int(self.square.get_bottom_right().y),
                  int(self.square.get_top_left().x):int(self.square.get_bottom_right().x)]
        if cv2.countNonZero(roi) != 0:
            self.marked = True

    def divide(self):
        if self.marked:
            side = self.square.side / 2
            square1 = Square(side, self.square.get_top_left())
            square2 = Square(side, Point(
                (self.square.get_top_left().x + (self.square.get_top_left().x + self.square.side)) / 2,
                self.square.get_top_left().y))
            square3 = Square(side, Point(self.square.get_top_left().x, (
                        self.square.get_top_left().y + (self.square.get_top_left().y + self.square.side)) / 2))
            square4 = Square(side, self.square.center)
            self.children.append(square1)
            self.children.append(square2)
            self.children.append(square3)
            self.children.append(square4)
            return square1, square2, square3, square4
