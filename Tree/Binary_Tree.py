class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)  # Initialize with a root node

    # In-order traversal (Left -> Root -> Right)
    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.data) + " -> ")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    # Pre-order traversal (Root -> Left -> Right)
    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.data) + " -> ")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    # Post-order traversal (Left -> Right -> Root)
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.data) + " -> ")
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Inorder Traversal look like this",tree.inorder_traversal(tree.root, ""))
print("Preorder Traversal looks like:", tree.preorder_traversal(tree.root, ""))
print("PostOrder Traversal looks like:", tree.postorder_traversal(tree.root, ""))
