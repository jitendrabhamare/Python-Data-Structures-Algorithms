# Binary Search Tree (BST)

***
<ins>**Example**</ins></br>
<img src="./Binary_search_tree.png" alt="drawing" width="250"/>

***
<ins>**Properties**</ins>
1. Exactly one node per key (value).
2. Each node has 3 attributes
    1. Key (value)
    2. Left Child Pointer
    3. Right Child Pointer
3. For any arbitrary node of a tree, the children in left sub-tree have keys less than the node-key and the children
in the right sub-tree have keys larger than the node key.

***
<ins>**Time-complexities Comparion of Sorted Arrays and BST Operations**</ins>

| Operations    | SortedArray-Running Time  |   BST-Running Time        |
|---------------|:-------------------------:|:-------------------------:|
| Search        |   O(log(n))               |   O(log(n))               |
| Select (given order statistic i) | O(1)   |   O(log(n))               |
| Min/Max       |   O(1)                    |   O(log(n))               |
| Predecessor/Successor |   O(1)            |   O(log(n))               |
| Rank*         | O(log(n))                 |   O(log(n))               |
| Output in Sorted Order|   O(n)            |   O(log(n))               |
| Insert        |   O(n)                    |   O(log(n))               |
| Delete        |   O(n)                    |   O(log(n))               |

*\*Rank is number of keys less than or equal to a given value. Thus for Sprted Array, do binary search and report position.*</br>

<ins>Note</ins>: Dynamic Dataset which involves lots of insert and delete operations, BST is better choice over sorted arrays. However, for static data, sorted arrays have upper hand.</br>

*** 
<ins>**BST Implementation**</ins>
- [here](./binary-search-tree.py)

Following methods are implemented. 
1. <ins>**search**</ins>
    - Traverse left/right child recursively as needed.
    - Return True if finds else False

2. <ins>**insert**</ins>
    - Compare the insert-node with each node and accordingly traverse through the tree and insert 

3. <ins>**delete**</ins>
    - binary search for new_key (k) 
     1. **Easy case**: if k has no children
        - Just delete k's node from tree. Done.
     2. **Medium case**: if k's node has one child
        - Just "splice out" k's node.
        - Unique child assumes position previously held by k's node
     3. **Difficult case**: k's node has two children
        - Compute k'e predecessor (l).
        - swap k with l.

4. <ins>**get_min**</ins>
    - Get min from the node. By default, it starts from the root. 
    - Start at the node. 
    - Follow left child pointer until you cannot anymore.
    - Return the last key found

5. <ins>**get_max**</ins>
    - Get max from the node. By default, it starts from the root. 
    - Start at the node. 
    - Follow right child pointer until you cannot anymore.
    - Return the last key found

6. <ins>**get_successor**</ins>
    - This method finds successor of a node k with given key without the parent pointer.
    - Algorithm steps
    1. Starting from root node, the algorithm keeps track of 'speculative successor' for the case
        - where k's right subtree is empty. 
    2. Easy Case:
        - If k's right subtree is non-empty,
        - It returns min-key in the right subtree.
    3. Otherwise- difficult case:
        - Speculation is correct, and it returns speculative successor as a successor. 
    - **Benefit of speculation**: When we reach difficult case, we already have an answer. We need not redo 
          iteration to find successor from parents.

7. <ins>**get_predecessor**</ins>
8. <ins>**inorder_traversal**</ins>
9. <ins>**sizeof**</ins>
10. <ins>**order_statistic**</ins>



    
    
    
    


