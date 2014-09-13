__author__ = 'pratik'
class Node:
    left = None
    right = None
    data = None
    def __init__(self, data):
        self.data = data

class BinaryTree:
    root=None

    def get_root(self):
        return self.root

    def insert_root(self,node):
        self.root = node


    def get_parent(self, root, data, parent):
        if root.data == data:
            parent = root
            return parent

        if root.right:
            parent = self.get_parent(root.right, data, parent)
            if parent:
                if parent.data == data:
                    return parent

        if root.left:
            parent = self.get_parent(root.left, data, parent)
            if parent:
                if parent.data == data:
                        return parent

        return parent


    def inorder_traversal(self,root):
        if not root:
            return
        self.inorder_traversal(root.left)
        print root.data
        self.inorder_traversal(root.right)

def main():
    list_binary_tree = [(5,2,8), (8,7,9),(2,1,3)]
    bin_tree = BinaryTree()
    root = Node(5)

    bin_tree.insert_root(root)
    new_root = bin_tree.get_root()
    bin_tree.inorder_traversal(root)
    for nodes in list_binary_tree:
        parent_data = nodes[0]
        if nodes[1]:
            left_node = Node(nodes[1])
        if nodes[2]:
            right_node = Node(nodes[2])
        parent=None
        parent = bin_tree.get_parent(root, parent_data, parent)
        if parent:
            print "Got", parent, parent_data
            print "Inserting left node: ", nodes[1]
            parent.left = left_node
            print "Inserting right node: ", nodes[2]
            parent.right = right_node
            print parent.left
            print parent.right
        else:
            print parent_data, parent, 'not found'
    bin_tree.inorder_traversal(bin_tree.root)


main()


