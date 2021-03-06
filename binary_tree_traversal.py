class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(tree.root, find_val)

    def print_tree(self,order):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        self.order = order
        return self.preorder_print(tree.root, "",self.order)[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        """
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False
        """
        
        if start:
                return self.preorder_search(start.left, find_val)
                return self.preorder_search(start.right, find_val)
                if start.value == find_val:
                    return True
                
        return False
        
            

    def preorder_print(self, start, traversal, order):
        """Helper method - use this to create a 
        recursive print solution."""
        #preorder
        if order == 'preorder':
            if start:
                traversal += (str(start.value) + "-")
                traversal = self.preorder_print(start.left, traversal, order)
                traversal = self.preorder_print(start.right, traversal, order)
        
        #postorder
        elif order == 'postorder':
            if start:
                traversal = self.preorder_print(start.left, traversal,order)
                traversal = self.preorder_print(start.right, traversal, order)
                traversal += (str(start.value) + "-")
                
        elif order == 'inorder':
            if start:
                traversal = self.preorder_print(start.left, traversal,order)
                traversal += (str(start.value) + "-")
                traversal = self.preorder_print(start.right, traversal,order)
            
        return traversal
            

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# Test search
# Should be True
print tree.search(2)
# Should be False
print tree.search(3)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree('inorder')
