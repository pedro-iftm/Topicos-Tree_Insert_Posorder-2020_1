from node import Node


class Tree:
    def __init__(self, root_value, node_values):
        self.root = Node(root_value)
        self.insert(node_values)

    def __call__(self):
        self.pos_order(self.root)

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

    def pos_order(self, actual_node):
        if actual_node == None:
            return

        self.pos_order(actual_node.left)
        self.pos_order(actual_node.right)
        print(actual_node.value)
