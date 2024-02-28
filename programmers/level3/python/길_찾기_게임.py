import sys

sys.setrecursionlimit(10**6)


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
    nodes.sort(key=lambda node: (-node.y, node.x))  # Fix sorting order

    root = nodes[0]
    for node in nodes[1:]:
        current = root
        while True:
            if node.x < current.x:
                if not current.left:
                    current.left = node
                    break
                else:
                    current = current.left
                    continue

            elif node.x > current.x:
                if not current.right:
                    current.right = node
                    break
                else:
                    current = current.right
                    continue

    return root


def preorder(head, result=[]):
    if not head:
        return

    result.append(head.index)
    preorder(head.left, result)
    preorder(head.right, result)

    return result


def postorder(head, result=[]):
    if not head:
        return

    postorder(head.left, result)
    postorder(head.right, result)
    result.append(head.index)

    return result


def solution(nodeinfo):
    tree = get_tree(nodeinfo)

    return [preorder(tree), postorder(tree)]


print(
    solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
)
# root = nodes[0]
#     for node in nodes[1:]:
#         current = root
#         while True:
#             if node.x < current.x:
#                 if current.left is None:
#                     current.left = node
#                     break
#                 else:
#                     current = current.left
#             else:
#                 if current.right is None:
#                     current.right = node
#                     break
#                 else:
#                     current = current.right
