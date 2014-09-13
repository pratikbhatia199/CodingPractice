__author__ = 'pratik'

class Node:
    left = None
    right = None
    data = None
    def __init__(self, data):
        self.data = data

class BinaryTree:
    root=None
    dict_level_list = {}
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

    def add_to_linked_list_inorder(self, node, level):
        if node == None:
            return

        if level in self.dict_level_list:
            list_level = self.dict_level_list[level]
            list_level.append(node.data)
            self.dict_level_list[level] = list_level

        else:
            self.dict_level_list[level] = [node.data]


    def inorder_create_list(self, node, level):
        if node==None:
            return
        self.inorder_create_list(node.left, level+1)
        self.add_to_linked_list_inorder(node, level)
        self.inorder_create_list(node.right, level+1)




def main():
    list_binary_tree = [(5,2,8),(2,1,3),(8,7,9)]
    bin_tree = BinaryTree()
    root = Node(5)
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
    bin_tree.inorder_create_list(bin_tree.root, 0)
    print bin_tree.dict_level_list






main()
