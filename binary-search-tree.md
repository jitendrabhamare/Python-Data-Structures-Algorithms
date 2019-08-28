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



    
    
    
    


