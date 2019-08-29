### Binary Search Tree Implementation 
### Author: Jitendra Bhamare

## Queue class to help print BST
from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


## Define a Node 
class Node(object):
    
    # Constructor with 3 properties 
    def __init__(self, key=None):
        self.key   = key
        self.left  = None
        self.right = None

    """ basic methods """

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key
    
    def set_left_child(self, node):
        self.left = node
        
    def set_right_child(self, node):
        self.right = node
    
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
     # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_key()})"

## Define a tree class here
class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, key):
        self.root = Node(key)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """  0: new_node eq node 
            -1: new_node <  node
             1: new_node >  node
        """
        if new_node.get_key() == node.get_key():
            return 0
        elif new_node.get_key() < node.get_key():
            return -1
        else:
            return 1

    ## Search Operation 
    def search(self, key):
        """
        - Start at root. 
        - Traverse left/right child recursively as needed.
        - Return True if finds else False
        """

        root_node   = self.get_root()
        search_node = Node(key)
        result = self.search_recursively(root_node, search_node)
        return result

    def search_recursively(self, node, search_node):
        """
        The recursive helper function of search
        Traverse left/right using comparison
        """

        comparison = self.compare(node, search_node)

        if comparison == 0:
            return True
        elif comparison == -1: # traverse left
            if node.has_left_child():
                return self.search_recursively(node.get_left_child(), search_node)
            else:
                return False
        else: #i.e. if comparison == 1, traverse right
            if node.has_right_child():
                return self.search_recursively(node.get_right_child(), search_node)
            else:
                return False


    ## Insert a new node in BST
    def insert(self,new_key):
        """
        Used while loop to implement. 
        Can also use recursion instead, as used in search function. 
        Compare the insert-node with each node and accordingly traverse through the tree and insert 
        """
        new_node = Node(new_key)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node
                node = new_node
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping          

    def get_min(self, node=None):
        """
        - Get min from the node. By default, it starts from the root. 
        - Start at the node. 
        - Follow left child pointer until you cannot anymore.
        - Return the last key found
        """
        if node is None:
            node = self.get_root()
        while(node.get_left_child()):
            node = node.get_left_child()

        return node.get_key()


    def get_max(self, node=None):
        """
        - Get max from the node. By default, it starts from the root. 
        - Start at the node. 
        - Follow right child pointer until you cannot anymore.
        - Return the last key found
        """
        if node is None:
            node = self.get_root()
        while(node.get_right_child()):
            node = node.get_right_child()

        return node.get_key()

    def get_successor(self, node, key):
        """ 
        - If node has right subtree, return max key from subtree
        - 
        
        change to iterative
        add tentative succ 
        """

        ## Base case
        if node is None:
            return

        ## If key is present at node
        if node.get_key() == key:
            # the min value of right subtree is successor
            if node.has_right_child():
                succ = self.get_min(node.get_right_child())
                return succ


        ## If key is smaller than node-key, look into left subtree
        elif key < node.get_key():
            return self.get_successor(node.get_left_child(), key)

        ## If key is larger than node-key, look into right subtree
        else:
            return self.get_successor(node.get_right_child(), key)


    ### Print Tree (with the help of queue DS)
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

        return s




#---------------------------------------------------------------------------------------------
#   Testcase 
#---------------------------------------------------------------------------------------------

tree = Tree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)
print(f"""
search for 8: {tree.search(8)}
search for 2: {tree.search(2)}
""")
print(tree)

## Get root
root = tree.get_root()


## Find min/max of tree
min_val = tree.get_min()
max_val = tree.get_max()
print("Min-val: {}".format(min_val))
print("Max-val: {}".format(max_val))

## Get Successor
succ1 = tree.get_successor(root, 7)
print(succ1)









