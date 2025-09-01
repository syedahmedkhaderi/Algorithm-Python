class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
class BST():
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        curr = self.root
        while True:
            if new_node.data > curr.data:
                if curr.right is None:
                    curr.right = new_node
                    break
                else:
                    curr = curr.right
            elif new_node.data < curr.data:
                if curr.left is None:
                    curr.left = new_node
                    break
                else:
                    curr = curr.left
            else:
                break
                # Duplicate value

    def lookup(self, val):
        curr = self.root
        while curr is not None:
            if curr.data == val:
                return "found"
            elif curr.data < val:
                curr = curr.right
            else:
                curr = curr.left
        return "Not found"
            
    
tree = BST()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.inorder(tree.root,[]))
print(tree.preorder(tree.root,[]))
print(tree.postorder(tree.root,[]))
