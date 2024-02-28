class TreeNode:
    def __init__(self, index, x, y, left=None, right=None):
        self.index = index
        self.x = x
        self.y = y
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.index}"

    def __repr__(self) -> str:
        return self.__str__()


def get_tree(nodeinfo: list):
    nodes = [TreeNode(i + 1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda node: (node.y, -node.x))

    head = nodes.pop()
    parents = [head]

    def find_parent(parents, child):
        for parent in parents:
            if not parent.left and not parent.right and child.x < parent.x:
                parent.left = child
                return

            elif not parent.right and child.x > parent.x:
                parent.right = child
                return

    while nodes:
        children = [nodes.pop()]
        while nodes and nodes[-1].y == children[0].y:
            children.append(nodes.pop())

        for child in children:
            find_parent(parents, child)

        parents = children

    return head


def preorder(head, result=[]):
    if not head:
        return

    print(head.index, head.left, head.right)

    result.append(head.index)
    preorder(head.left, result)
    preorder(head.right, result)

    return result


def postorder(head, result=[]):
    if not head:
        return

    preorder(head.left, result)
    preorder(head.right, result)
    result.append(head.index)

    return result


def solution(nodeinfo):
    tree = get_tree(nodeinfo)
    print(tree)

    return [preorder(tree), postorder(tree)]


print(
    solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
)
