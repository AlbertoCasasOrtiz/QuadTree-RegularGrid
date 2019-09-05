import math

from node.Node import Node
from square.Square import Point
from square.Square import Square


class RegularGrid:

    def __init__(self):
        self.nodes = []
        self.adjacency = []

    def get_num_marked(self):
        num = 0
        for node in self.nodes:
            if node.marked:
                num += 1
        return num

    def create_regular_grid(self, img, horizontal_tiles, show_marked):
        height_image = img.shape[0]
        width_image = img.shape[1]
        current_x = 0
        current_y = 0
        side = width_image / horizontal_tiles
        square = Square(side, Point(current_x, current_y))
        vertical_tiles = height_image / side
        node = Node(square)
        node.mark(img)
        if show_marked or not node.marked:
            self.nodes.append(node)

        for i in range(0, int(math.ceil(vertical_tiles))):
            for j in range(0, int(horizontal_tiles)):

                square = Square(side, Point(current_x, current_y))
                node = Node(square)
                node.mark(img)
                if show_marked or not node.marked:
                    self.nodes.append(node)
                current_x += side
            current_x = 0
            current_y += side

    def calculate_adjacency(self):
        for i in range(len(self.nodes)):
            self.adjacency.append([])
            for j in range(len(self.nodes)):
                if self.nodes[i] is not self.nodes[j]:
                    print(self.nodes[i].square.center.distance(self.nodes[j].square.center))
                    print(self.nodes[i].square.side)
                    if self.nodes[i].square.center.distance(self.nodes[j].square.center) <= self.nodes[
                                  i].square.side + 0.1:
                        self.adjacency[i].append(j)

    def print_adjacents(self):
        file = open("out/regulargrid-adjacents.txt", "w")

        for i in self.adjacency:
            for j in i:
                file.write(str(j) + " ")
            file.write("\n")

        file.close()

    def print_nodes(self):
        file = open("out/regulargrid-nodes.txt", "w")

        file.write(str(self.nodes[0].square.side) + "\n")

        for n in self.nodes:
            file.write(str(n.square.center.x) + " " + str(n.square.center.y) + "\n")

        file.close()
