__author__ = 'pratik'
class Node:

    left = None
    right = None
    data  = None
    def __init__(self, data):
        self.data = data

class BinarySearchTree:

    root = None

    def insert(self, node):
        if not self.root:
            self.root = node
            return
        current_node = self.root
        parent_node = None

        while(current_node!=None):
            if node.data < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right

        if node.data < parent_node.data:
            parent_node.left = node
        else:
            parent_node.right = node

    def get_max_height(self, root):
        if root:
            if root.left==None and root.right == None:
                return 1
            if self.get_max_height(root.left) > self.get_max_height(root.right):
                return self.get_max_height(root.left)+1
            else:
                return self.get_max_height(root.right)+1

    def preorder(self, root):
        if root:
            print root.data
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder_traversal(self, node):
        if not node:
            return
        self.inorder_traversal(node.left)
        print node.data
        self.inorder_traversal(node.right)

    def get_max_diameter_of_tree(self, root):
        if not root.left and not root.right:
            return (1, 1)

        print root.data, "current root"
        left_height = 0
        right_height = 0
        max_diameter_left = 0
        max_diameter_right = 0
        if root.left:
            left_height, max_diameter_left = self.get_max_diameter_of_tree(root.left)

        if root.right:
            right_height, max_diameter_right = self.get_max_diameter_of_tree(root.right)

        return (max(left_height, right_height)+1, max((left_height+right_height+1), max_diameter_left, max_diameter_right))



def main():
    bst = BinarySearchTree()
    #list_values = [50, 30, 60, 29, 35, 70, 33, 36,100, 75,110,71, 76]
    list_values = [80, 30, 90, 25, 35, 100, 20, 29, 40, 27, 36, 45, 26, 28, 50, 60, 70]
    for value in list_values:
        n = Node(value)
        bst.insert(n)
    print "inorder"
    bst.inorder_traversal(bst.root)
    print "preorder"
    bst.preorder(bst.root)

    print bst.get_max_height(bst.root)

    print bst.get_max_diameter_of_tree(bst.root), "max height"

main()