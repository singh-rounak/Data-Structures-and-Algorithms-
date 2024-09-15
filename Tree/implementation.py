class Node:
    def __init__(self, value):
        self.left =None
        self.value = value
        self.right = None


class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            self.createNode(data)
        if data < node:
            node.left = self.insert(node.left, data)
        else: 
            node.right=self.insert(node.right,data)
        
