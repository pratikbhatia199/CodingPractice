__author__ = 'pratik'

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

    def get_max_depth(self, root):
        if root == None:
            return 0
        return max(self.get_max_depth(root.left), self.get_max_depth(root.right)) + 1

    def is_balanced(self, root, balanced):
        if balanced == False:
            return balanced
        print root
        if root == None:
            return balanced
        print root.data

        balance = self.get_max_depth(root.left) == self.get_max_depth(root.right)
        recursion = self.is_balanced(root.left, balanced) and self.is_balanced(root.right, balanced)
        return balanced and balance and recursion

    def inorder_traversal(self,root):
        if not root:
            return
        self.inorder_traversal(root.left)
        print root.data
        self.inorder_traversal(root.right)

    def LCA(self, root, p, q, result):
        print "Root: ", root, p, q, result
        if result:
            print "result already present"
            return result

        if root==None:
            return None

        print "Root data:", root.data
        if root.data == p or root.data == q:
            print "Something equal", root.data, p, q
            return root
        print "Calling left root", root.left, p, q, result
        left_root = self.LCA(root.left, p, q, result)
        print "Calling right root", root.right, p, q, result
        right_root = self.LCA(root.right, p, q, result)

        if left_root and right_root:
            result = root
            print "Result found, should stop", result.data
            return result

        if left_root:
            return left_root
        else:
            return right_root

def main():
    list_binary_tree = [(10, 8, 2), (8, 3, 5), (2, 9, ''), (3, 12, 13)]
    bin_tree = BinaryTree()
    root = Node(list_binary_tree[0][0])
    bin_tree.insert_root(root)
    new_root = bin_tree.get_root()
    bin_tree.inorder_traversal(root)
    for nodes in list_binary_tree:
        parent_data = nodes[0]
        left_node=None
        right_node=None
        if nodes[1]:
            left_node = Node(nodes[1])
        if nodes[2]:
            right_node = Node(nodes[2])
        parent=None
        parent = bin_tree.get_parent(root, parent_data, parent)
        if parent:
            print "Got", parent, parent_data
            if left_node:
                print "Inserting left node: ", nodes[1]
                parent.left = left_node

            if right_node:
                print "Inserting right node: ", nodes[2]
                parent.right = right_node
            print parent.left
            print parent.right
        else:
            print parent_data, parent, 'not found'

    bin_tree.inorder_traversal(bin_tree.root)
    print "Max depth: ",bin_tree.get_max_depth(bin_tree.root)
    value =  bin_tree.is_balanced(bin_tree.root, True)
    print "Is balanced ", value
    node = bin_tree.LCA(bin_tree.root, 8, 10, None)
    print node
    if node:
        print node.data




main()


