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
            print "Root inserted", node
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

        if node.data <= parent_node.data:
            print node.data, "inserted left of ", parent_node.data
            parent_node.left = node
        else:
            print node.data, "inserted right of ", parent_node.data
            parent_node.right = node


    def inorder_traversal(self, node):
        if not node:
            return
        self.inorder_traversal(node.left)
        print node.data
        self.inorder_traversal(node.right)

    def get_max_height(self, root):
        if root.left==None and root.right == None:
            return 1
        if self.get_max_height(root.left) > self.get_max_height(root.right):
            return self.get_max_height(root.left)+1
        else:
            return self.get_max_height(root.right)+1



def insert_in_BST(start_index, last_index, list_sorted, bst):
    if start_index > last_index:
        return

    mid = (start_index+last_index)/2
    print mid, start_index, last_index
    node = Node(list_sorted[mid])

    print "Inserting ", node, node.data
    bst.insert(node)
    insert_in_BST(start_index, mid-1, list_sorted, bst)
    insert_in_BST(mid+1,last_index,list_sorted, bst)




def main():

    list_sorted = [1,2,3,5,7,8,9]
    bst = BinarySearchTree()
    insert_in_BST(0, len(list_sorted)-1, list_sorted, bst)

    start = bst.root
    bst.inorder_traversal(start)
    print bst.get_max_height(start)

main()







