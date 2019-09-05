import cv2

from square.Point import Point


class Square:

    def __init__(self, side, top_left):
        self.side = side
        self.top_left = top_left
        self.center = Point((top_left.x + (top_left.x + side)) / 2, (top_left.y + (top_left.y + side)) / 2)

    def get_center(self):
        return self.center

    def get_top_left(self):
        return self.top_left

    def get_top_right(self):
        return Point(self.top_left.x + self.side, self.top_left.y)

    def get_bottom_left(self):
        return Point(self.top_left.x, self.top_left.y + self.side)

    def get_bottom_right(self):
        return Point(self.top_left.x + self.side, self.top_left.y + self.side)

    def draw_square(self, img, color, thickness):
        cv2.rectangle(img, (int(self.get_top_left().x), int(self.get_top_left().y)),
                      (int(self.get_bottom_right().x), int(self.get_bottom_right().y)), color, thickness)
        cv2.line(img, (int(self.center.x), int(self.center.y)), (int(self.center.x), int(self.center.y)), color,
                 thickness + 1)
