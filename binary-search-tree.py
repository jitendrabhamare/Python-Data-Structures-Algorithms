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

    def delete(self, new_key):
        """
        -  binary search for new_key (k) 
        1. Easy case: if k has no children
           - Just delete k's node from tree. Done.
        2. Medium case: if k's node has one child
           - Just "splice out" k's node.
           - Unique child assumes position previously held by k's node
        3. Difficult case: k's node has two children
           - Compute k'e predecessor (l).
           - swap k with l.
        """
        new_node = Node(new_key)
        node = self.get_root()
        parent = None

        # base case
        if node is None:
            return

        while (node):
            comparison = self.compare(node, new_node)
            
            if comparison == 0:
                ## perform deletion if match
                # Easy case
                if node.left == None and node.right == None:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    break

                # Medium case
                if node.left and node.right == None:
                    if parent.left == node:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                    break

                if node.left == None and node.right:
                    if parent.left == node:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                    break

                # Difficult case
                if node.left and node.right:
                    print("DIfficult case -yo")
                    # Find k's predecessor 
                    pred_parent = node
                    pred = node.left
                    while(pred.right):
                        pred_parent = pred
                        pred = pred.right
                    
                    # swap keys of node and pred
                    pred.key, node.key = node.key, pred.key

                    # remove pred
                    if pred_parent.left == pred:
                        pred_parent.left = None
                    if pred_parent.right == pred:
                        pred_parent.right = None
                   
                    break


            elif comparison == -1:
                ## go left
                parent = node
                node = node.get_left_child()

            else: 
                ## go right
                parent = node
                node = node.get_right_child()
        


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
        - This method finds successor of a node k with given key without the parent pointer.
        - Algorithm steps
            1. Starting from root node, the algorithm keeps track of 'speculative successor' for the case
            where k's right subtree is empty. 
            2. Easy Case:
                If k's right subtree is non-empty,
                It returns min-key in the right subtree.
            3. Otherwise- difficult case:
                Speculation is correct, and it returns speculative successor as a successor. 
        - Benefit of speculation: When we reach difficult case, we already have an answer. We need not redo 
          iteration to find successor from parents.
        """
        speculative_succ = None
        succ = None
        while (node):
            ## If key is present at node
            if node.get_key() == key:
                # the min value of right subtree is successor
                if node.has_right_child():
                    succ = self.get_min(node.get_right_child())
                else:
                    succ = speculative_succ
                break
                            
            ## If key is smaller than node-key, look into left subtree
            elif key < node.get_key():
                speculative_succ = node.get_key()
                node = node.get_left_child()

            ## If key is larger than node-key, look into right subtree
            else:
                node = node.get_right_child()

        return succ

    def get_predecessor(self, node, key):
        """ 
        - This method finds predecessor of a node k with given key without the parent pointer.
        - Algorithm steps
            1. Starting from root node, the algorithm keeps track of 'speculative predecessor' for the case
            where k's left subtree is empty. 
            2. Easy Case:
                If k's left subtree is non-empty,
                It returns max-key in the left subtree.
            3. Otherwise- difficult case:
                Speculation is correct, and it returns speculative predecessor as a predecessor. 
        - Benefit of speculation: When we reach difficult case, we already have an answer. We need not redo 
          iteration to find predecessor from parents.
        """
        speculative_pred = None
        pred = None
        while (node):
            ## If key is present at node
            if node.get_key() == key:
                # the max value of left subtree is predecessor
                if node.has_left_child():
                    pred = self.get_max(node.get_left_child())
                else:
                    pred = speculative_pred
                break
                            
            ## If key is smaller than node-key, look into left subtree
            elif key < node.get_key():
                node = node.get_left_child()

            ## If key is larger than node-key, look into right subtree
            else:
                speculative_pred = node.get_key()
                node = node.get_right_child()
            
        return pred


    def inorder_traversal(self, node=None):
        """
        Prints out keys in increasing order
        """
        if node is None:
            node = self.get_root()
        # Recurse left
        if node.has_left_child():
            self.inorder_traversal(node.get_left_child())
        print(node.get_key())
        if node.has_right_child():
            self.inorder_traversal(node.get_right_child())
        return
    
    def sizeof(self, node):
        """
        Return total number of nodes under a node
        """
        if node is None:
            return 0
        return 1 + self.sizeof(node.left) + self.sizeof(node.right)

    def order_statistic(self, i, node=None):
        """
        Finds ith order statstic of a tree
        """
        if node is None:
            node = self.get_root()

        s = self.sizeof(node.left)
        
        if s == i-1:
            return node.get_key()

        elif s >= i:
            return self.order_statistic(i, node.left)

        else:
            return self.order_statistic(i-s-1, node.right)


        
        

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
## create a tree (insert)
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

key_list = [1, 8, 3, 7, 13, 14]
## Get Successor
for key in key_list:
    succ = tree.get_successor(root, key)
    print("successor of {} is {}".format(key, succ))

## Get Predecessor
for key in key_list:
    pred = tree.get_predecessor(root, key)
    print("predecessor of {} is {}".format(key, pred))


## in-order traversal
tree.inorder_traversal()

## Delete a node
tree.delete(6)
print(tree)


## sizeof
size = tree.sizeof(root)
print("size of tree: {}".format(size))


## order statistic
for i in range(1,10):
    order = tree.order_statistic(i)
    print("{} th order statistic of tree: {}".format(i, order))









