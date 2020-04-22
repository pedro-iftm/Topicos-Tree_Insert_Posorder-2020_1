from node import Node


class Tree:
    def __init__(self, root_value, node_values):
        self.root = Node(root_value)
        self.insert(node_values)
        self.positive_numbers = []

    def __call__(self):
        print('pos order')
        self.pos_order(self.root, True)
        print('\nheight')
        height = self.get_height(self.root)
        print(height)
        print('\npositive numbers')
        print(self.positive_numbers)

    def insert(self, node_values):
        for value in node_values:
            actual_node = self.root
            new_node = Node(value)

            while True:
                last_node = actual_node

                if value < actual_node.value:
                    actual_node = last_node.left

                    if actual_node is None:
                        actual_node = new_node
                        last_node.left = new_node
                        break

                else:
                    actual_node = last_node.right

                    if actual_node is None:
                        actual_node = new_node
                        last_node.right = new_node
                        break

    def pos_order(self, actual_node, save_positive_numbers=False):
        if actual_node == None:
            return

        self.pos_order(actual_node.left, save_positive_numbers)
        self.pos_order(actual_node.right, save_positive_numbers)
        print(actual_node.value)

        if save_positive_numbers:
            self.__set_positive_numbers(actual_node.value)

    def __set_positive_numbers(self, value):
        if value >= 0:
            self.positive_numbers.append(value)

    def get_height(self, actual_node):
        if actual_node == None or actual_node.left == None and actual_node.right == None:
            return 0

        else:
            return 1 + (self.get_height(actual_node.left)
                        if self.get_height(actual_node.left) > self.get_height(actual_node.right)
                        else self.get_height(actual_node.right))