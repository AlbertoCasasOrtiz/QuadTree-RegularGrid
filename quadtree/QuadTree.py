from node.Node import Node
from square.Square import Square, Point


class QuadTree:

    def __init__(self):
        self.nodes = []

    def get_num_marked(self):
        num = 0
        for node in self.nodes:
            if node.marked:
                num += 1
        return num

    def create_quad_tree(self, img, depth, show_marked):
        width_image = img.shape[1]
        current_x = 0
        current_y = 0
        current_depth = 0
        side = width_image
        square = Square(side, Point(current_x, current_y))
        node = Node(square)
        node.mark(img)
        self.nodes.append(node)

        while self.get_num_marked() > 0 and current_depth < depth:
            new_nodes = []
            aux_list = self.nodes.copy()
            for n in self.nodes:
                if n.marked:
                    s1, s2, s3, s4 = n.divide()
                    s1 = Node(s1)
                    s1.mark(img)
                    s2 = Node(s2)
                    s2.mark(img)
                    s3 = Node(s3)
                    s3.mark(img)
                    s4 = Node(s4)
                    s4.mark(img)
                    aux_list.remove(n)
                    if show_marked or current_depth < depth - 1:
                        new_nodes = new_nodes + [s1, s2, s3, s4]
            self.nodes = aux_list
            self.nodes = self.nodes + new_nodes
            new_nodes.clear()
            current_depth += 1
