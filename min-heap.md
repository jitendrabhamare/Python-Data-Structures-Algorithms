# Heap 

### The Heap Property 
- Conceptually think of a heap as a tree. </br>
> Rooted, binary, as complete as possible. </br>
>
> At Every Node X, key[X] <= all keys of X's children
>
> X may have 0, 1 or 2 children. </br>
> For a given dataset, the Heap may not be unique but The root has to have a minimum value key. </br>

- Array Implementation 
> parent of i = Floor value of i/2. </br>

### Heap Operations
1. Push
  - Stick a new node (k) at the end of the last level.
  - bubbble-up (heapify_up) until heap property is restored. 
  
2. Pop 
  - Delete Root
  - Move last leaf to be new root
  - Iteratively bubble-down (heapify_down) until heap property is restored. 
  
### Run Time
- O(log(height))


### Code
- [MinHeap](https://github.com/jitendrabhamare/Python-Data-Structures-Algorithms/blob/master/MinHeap.py)
