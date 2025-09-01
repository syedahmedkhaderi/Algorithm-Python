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
            
    def inOrder_Traversal(self, curr, mylist):
        while curr is not None: #Base case is Curr = None
            self.inOrder_Traversal(curr.left, mylist)
            mylist.append(curr.data)
            self.inOrder_Traversal(curr.right, mylist)
        return mylist

    def preOrder_Traversal(self, curr, mylist):
        while curr is not None: #Base case is Curr = None
            mylist.append(curr.data)
            self.inOrder_Traversal(curr.left, mylist)
            self.inOrder_Traversal(curr.right, mylist)
        return mylist
    
    def postOrder_Traversal(self, curr, mylist):
        if curr.left:
            self.preOrder_Traversal(curr.left, mylist)
        if curr.right:
            self.preOrder_Traversal(curr.right, mylist)
        mylist.append(curr.data)
        return mylist



tree = BST()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.inOrder_Traversal(tree.root,[]))
print(tree.preOrder_Traversal(tree.root,[]))
print(tree.postOrder_Traversal(tree.root,[]))

'''
            5
        3       7
    1               13
0                10     65
'''
#Inorder traversal for this tree : [0, 1, 3, 5, 7, 10, 13, 65]
#Preorder Traversal for this tree : [5, 3, 1, 0, 7, 13, 10, 65]
#Postorder Traversal for this tree : [0, 1, 3, 10, 65, 13, 7, 5]