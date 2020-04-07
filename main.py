from tree import Tree


def get_user_input():
    nodes = []
    counter = 0

    root = int(input('Informe a raíz da árvore: '))
    node_quantity = int(input('Informe a quantidade de nós: '))

    while counter < node_quantity:
        counter += 1
        node = int(input(f'Informe o valor do nó ({counter}/{node_quantity}): '))
        nodes.append(node)

    return root, nodes


if __name__ == "__main__":
    root, nodes = get_user_input()
    tree = Tree(root, nodes)
    tree()
